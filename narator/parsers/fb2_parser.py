import logging
import time
from typing import Generator

import bs4
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from narator.parsers.base_parser import BaseParser, get_driver

logger = logging.getLogger(__name__)


class Fb2Parser(BaseParser):
    SOUP_CONTENT = 'section'
    SOUP_TITLE = 'section>h3>span'
    CONTENT = '//section'
    TITLE = '//section/h3/span'
    NEXT_BUTTON = "//a[contains(@class, 'btn') and contains(text(), 'Далее >')]"
    MODAL = '//*[@id="modalSocials"]'
    MODAL_CLOSE_BTN = '//*[@id="modalSocials"]//button[@aria-label="Close"]'

    def _walk_pages(self, start_url: str) -> Generator[str, None, None]:
        driver = get_driver()
        driver.set_page_load_timeout(30.0)
        driver.get(start_url)
        try:
            while True:
                try:
                    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, self.CONTENT)))
                    yield driver.page_source
                    time.sleep(0.5)
                    modal = driver.find_element('xpath', self.MODAL)
                    if modal and modal.is_displayed():
                        driver.find_element('xpath', self.MODAL_CLOSE_BTN).click()

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
