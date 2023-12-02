import time
import logging

import bs4
from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from narator.storage import add_chapter, add_book_if_not_exist

_driver, _service = None, None
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
CONTENT = '#chr-content'
TITLE = '.chr-title'


def get_driver():
    global _driver, _service
    if not _service:
        _service = Service(executable_path=ChromeDriverManager().install())
    if not _driver:
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')
        options.add_argument('--crash-dumps-dir=/tmp')
        options.add_argument('--disable-crash-reporter')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        _driver = webdriver.Chrome(service=_service, options=options)
        _driver.set_page_load_timeout(15)
    return _driver


def walk_pages(start_url: str):
    driver = get_driver()
    driver.get(start_url)
    try:
        while True:
            try:
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, CONTENT)))
                yield driver.page_source
                time.sleep(0.5)
                driver.find_element('id', 'next_chap').click()

            except TimeoutException as e:
                logger.error(e)
                break
    except WebDriverException as e:
        logger.error(e)
        pass
    finally:
        driver.quit()
        _driver, _service = None, None
        print('Driver closed')


def parse_page(html_data: str) -> dict:
    soup = bs4.BeautifulSoup(html_data, 'html.parser')
    text = ''
    content = soup.select_one(CONTENT)
    for i in content.find_all('p'):
        text += i.text + '\n'
    title = soup.select_one(TITLE).text

    _, chapter_id, *_ = title.split(' ')
    for i in ';:-':
        chapter_id = chapter_id.replace(i, '')

    return {
        'chapter_number': int(chapter_id),
        'text': text,
        'title': title,
        'book_id': 1,
    }


if __name__ == '__main__':
    start_url = 'https://readnovelfull.me/the-mech-touch/chapter-1-age-of-mechs/'
    add_book_if_not_exist(1, 'The Mech Touch')
    for page in walk_pages(start_url=start_url):
        page_data = parse_page(page)
        add_chapter(**page_data)
        logger.info('Saved data for chapter %s', page_data['chapter_number'])
