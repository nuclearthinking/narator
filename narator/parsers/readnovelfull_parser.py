import time
import logging
from typing import Generator

import bs4
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from narator.parsers.base_parser import BaseParser, get_driver

logger = logging.getLogger(__name__)


class ReadNovelFullParser(BaseParser):
    CONTENT = '#chr-content'
    TITLE = '.chr-title'

    def _walk_pages(self, start_url: str) -> Generator[str, None, None]:
        driver = get_driver()
        driver.get(start_url)
        try:
            while True:
                try:
                    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, self.CONTENT)))
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

    def _parse_page(self, html_data: str) -> dict[str, str | int]:
        soup = bs4.BeautifulSoup(html_data, 'html.parser')
        text = ''
        content = soup.select_one(self.CONTENT)
        for i in content.find_all('p'):
            text += i.text + '\n'
        title = soup.select_one(self.TITLE).text

        _, chapter_id, *_ = title.split(' ')
        for i in ';:-':
            chapter_id = chapter_id.replace(i, '')

        return {
            'chapter_number': int(chapter_id),
            'text': text,
            'title': title,
        }
