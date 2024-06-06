from abc import ABCMeta, abstractmethod
from typing import Generator

import nodriver as uc
from rich import print as pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from narator.storage.base import add_chapter, add_book_if_not_exist
from narator.core.enums.narration_language import NarrationLanguage

_driver, _service = None, None


def get_driver(headless: bool = True):
    global _driver, _service
    if not _service:
        _service = Service(executable_path=ChromeDriverManager().install())
    if not _driver:
        options = Options()
        options.set_capability('pageLoadStrategy', 'none')
        options.add_argument('--no-sandbox')
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')
        options.add_argument('--crash-dumps-dir=/tmp')
        options.add_argument('--disable-crash-reporter')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        _driver = webdriver.Chrome(
            service=_service,
            options=options,
        )
        _driver.set_page_load_timeout(15)
    return _driver


def get_undetected_driver(headless: bool = True):
    options = Options()
    options.set_capability('pageLoadStrategy', 'none')
    options.add_argument('--no-sandbox')
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    options.add_argument('--crash-dumps-dir=/tmp')
    options.add_argument('--disable-crash-reporter')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')

    return uc.Chrome()


class BaseParser(metaclass=ABCMeta):
    def __init__(self, debug: bool = False):
        self._debug = debug

    @abstractmethod
    def _walk_pages(self, start_url: str) -> Generator[str, None, None]:
        raise NotImplementedError('Not implemented yet')

    @abstractmethod
    def _parse_page(self, html_data: str) -> dict[str, str | int]:
        raise NotImplementedError('Not implemented yet')

    def parse(self, start_url: str, book_id: int, book_name: str, language: NarrationLanguage) -> None:
        if not self._debug:
            add_book_if_not_exist(book_id=book_id, title=book_name, language=language.value)
        for html_data in self._walk_pages(start_url):
            chapter_data = self._parse_page(html_data)
            if not self._debug:
                add_chapter(
                    book_id=book_id,
                    title=chapter_data['title'],
                    text=chapter_data['text'],
                    chapter_number=chapter_data['chapter_number'],
                )
            text_length = len(chapter_data['text'])
            lines_count = len(chapter_data['text'].split('\n'))
            pprint(
                f'[blue] Chapter saved for book {book_name}, chapter '
                f'{chapter_data["chapter_number"]}, lines: {lines_count}, characters: {text_length}'
            )
