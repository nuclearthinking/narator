import re
import asyncio
import logging
from pprint import pprint

import bs4
import nodriver as uc

from narator.storage.base import add_chapter, add_book_if_not_exist
from narator.parsers.base_parser import BaseParser
from narator.core.enums.narration_language import NarrationLanguage

logger = logging.getLogger(__name__)


def extract_chapter_number(url):
    match = re.search(r'/chapter-(\d+)', url)
    if match:
        return match.group(1)
    return None


class LightNovelWorldParser(BaseParser):
    CONTENT = '#chapter-container'
    TITLE = 'span.chapter-title'
    NEXT_BUTTON = 'a.button.nextchap'

    COOKIE_MODAL = '#qc-cmp2-main > div'
    COOKIE_AGREE = '//span[text()="AGREE"]/parent::button'

    _browser = None
    _book_title = None

    async def _async_walk_pages(self, start_url: str):
        if self._browser is None:
            self._browser = await uc.start()

        page = await self._browser.get(start_url)
        pages_data = []
        while True:
            try:
                await page.find(self._book_title, best_match=True, timeout=30)
                pages_data.append(await page.get_content())
                if len(pages_data) >= 10:
                    return pages_data
                await asyncio.sleep(3)
                next_btn = await page.find('Next', best_match=True)
                await next_btn.click()
            except Exception as e:
                logger.error(e)
                return pages_data

    def _walk_pages(self, start_url: str):
        async def _i():
            data = await self._async_walk_pages(start_url)
            return data

        pages = asyncio.get_event_loop().run_until_complete(_i())

        return pages

    def _parse_page(self, html_data: str) -> dict[str, str | int]:
        soup = bs4.BeautifulSoup(html_data, 'html.parser')
        text = ''
        content = soup.select_one(self.CONTENT)
        if not content:
            raise Exception('Content not found')

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

    def parse(self, start_url: str, book_id: int, book_name: str, language: NarrationLanguage) -> None:
        self._book_title = book_name
        start_chapter = extract_chapter_number(start_url)
        url_base = start_url[: start_url.rfind(start_chapter)]
        if not self._debug:
            add_book_if_not_exist(book_id=book_id, title=book_name, language=language.value)
        last_chapter = ''
        while pages := self._walk_pages(start_url):
            for html_data in pages:
                chapter_data = self._parse_page(html_data)
                if not self._debug:
                    add_chapter(
                        book_id=book_id,
                        title=chapter_data['title'],
                        text=chapter_data['text'],
                        chapter_number=chapter_data['chapter_number'],
                    )
                    last_chapter = chapter_data['chapter_number']
                text_length = len(chapter_data['text'])
                lines_count = len(chapter_data['text'].split('\n'))
                pprint(
                    f'[blue] Chapter saved for book {book_name}, chapter '
                    f'{chapter_data["chapter_number"]}, lines: {lines_count}, characters: {text_length}'
                )
            start_url = url_base + str(last_chapter)
