# https://readli.net/chitat-online/?b=1167536&pg=1

import time
from typing import Generator

import bs4
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from sqlalchemy.testing.plugin.plugin_base import logging

from narator.parsers.base_parser import BaseParser, get_driver

logger = logging.getLogger(__name__)


class ReadliParser(BaseParser):
    SOUP_CONTENT = 'div.reading__text'
    SOUP_TITLE = 'section>h3>span'
    CONTENT = 'div.reading__text'
    TITLE = '//section/h3/span'
    NEXT_BUTTON = '//div[@class="page-nav"]//a[text()="Следующая"]'

    def _walk_pages(self, start_url: str) -> Generator[str, None, None]:
        driver = get_driver()
        driver.set_page_load_timeout(30.0)
        driver.get(start_url)
        try:
            while True:
                try:
                    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, self.CONTENT)))
                    yield driver.page_source
                    time.sleep(0.5)

                    next_btn = driver.find_element('xpath', self.NEXT_BUTTON)
                    driver.execute_script('arguments[0].scrollIntoView();', next_btn)
                    next_btn.click()

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
        text = soup.select_one(self.SOUP_CONTENT).text
        title = soup.select_one(self.SOUP_TITLE).text

        _, chapter_id, *_ = title.split(' ')
        for i in ';:-':
            chapter_id = chapter_id.replace(i, '')

        return {
            'chapter_number': int(chapter_id),
            'text': text,
            'title': title,
        }
