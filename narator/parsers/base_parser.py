from abc import ABCMeta, abstractmethod
from typing import Generator

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from narator.core.enums.narration_language import NarrationLanguage
from narator.storage.base import add_chapter, add_book_if_not_exist

_driver, _service = None, None


def get_driver():
    global _driver, _service
    if not _service:
        _service = Service(executable_path=ChromeDriverManager().install())
    if not _driver:
        options = Options()
        options.set_capability('pageLoadStrategy', 'none')
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
        _driver = webdriver.Chrome(service=_service, options=options, )
        _driver.set_page_load_timeout(15)
    return _driver


class BaseParser(metaclass=ABCMeta):
    @abstractmethod
    def _walk_pages(self, start_url: str) -> Generator[str, None, None]:
        raise NotImplementedError('Not implemented yet')

    @abstractmethod
    def _parse_page(self, html_data: str) -> dict[str, str | int]:
        raise NotImplementedError('Not implemented yet')

    def parse(self, start_url: str, book_id: int, book_name: str, language: NarrationLanguage) -> None:
        add_book_if_not_exist(book_id=book_id, title=book_name, language=language.value)
        for html_data in self._walk_pages(start_url):
            chapter_data = self._parse_page(html_data)
            add_chapter(
                book_id=book_id,
                title=chapter_data['title'],
                text=chapter_data['text'],
                chapter_number=chapter_data['chapter_number'],
            )
