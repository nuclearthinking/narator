from tempfile import NamedTemporaryFile
from typing import Generator

from pydub import AudioSegment
from speechkit import configure_credentials
from speechkit.common.utils import creds

from narator.settings import settings
from narator.storage.base import Chapter
from narator.core.text_tools import characters_limited_book_iterator
from narator.core.narators.base_narrator import BaseNarrator
from speechkit import model_repository

from narator.core.text_tools import characters_limited_book_iterator

configure_credentials(
    yandex_credentials=creds.YandexCredentials(
        api_key=settings.yandex_token,
    )
)


class YandexNarrator(BaseNarrator):
    def __init__(
        self,
        characters_limit: int = 4900,
        paragraph_delay: int = 1000,
        sentence_delay: int = 100,
    ):
        self.characters_limit = characters_limit
        self.paragraph_delay = paragraph_delay
        self.sentence_delay = sentence_delay
        self._init_model()

    def _init_model(self):
        model = model_repository.synthesis_model()
        model.voice = 'anton'
        model.role = 'neutral'
        self._model = model

    def chapter_iterator(self, text: str) -> tuple[str, int]:
        for text, delay in characters_limited_book_iterator(
            text=text,
            characters_limit=self.characters_limit,
            paragraph_delay=self.paragraph_delay,
            sentence_delay=self.sentence_delay,
        ):
            yield text, delay

    def narrate(self, chapter: Chapter) -> AudioSegment:
        segment = None
        delay = 0
        for text, next_delay in self.chapter_iterator(chapter.text):
            next_segment = self._model.synthesize(text, raw_format=False)
            if segment is None:
                segment = next_segment
                continue
            segment = segment.append(
                AudioSegment.silent(duration=delay, frame_rate=segment.frame_rate),
                crossfade=0,
            )
            segment = segment.append(next_segment, crossfade=0)
            delay = next_delay
        return segment
