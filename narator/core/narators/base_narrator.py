from abc import ABCMeta, abstractmethod
from typing import Generator

from pydub import AudioSegment

from narator.storage.base import Chapter


class BaseNarrator(metaclass=ABCMeta):
    @abstractmethod
    def chapter_iterator(self, text: str) -> Generator[tuple[str, int], None, None]:
        raise NotImplementedError('Not implemented yet.')

    @abstractmethod
    def narrate(self, chapter: Chapter) -> AudioSegment:
        raise NotImplementedError('Not implemented yet.')
