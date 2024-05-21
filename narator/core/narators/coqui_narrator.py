from tempfile import NamedTemporaryFile

import torch
from pydub import AudioSegment
from TTS.api import TTS

from narator.settings import settings
from narator.exceptions import UnableToNarrateException
from narator.storage.base import Chapter
from narator.core.text_tools import is_wordless_line, per_sentence_book_iterator
from narator.core.narators.base_narrator import BaseNarrator
from narator.core.enums.narration_artists import NarrationArtists
from narator.core.enums.narration_language import NarrationLanguage

_CHARACTER_LIMIT_MAP = {
    NarrationLanguage.en: 250,
    NarrationLanguage.ru: 182,
}


class CoquiNarrator(BaseNarrator):
    def __init__(
        self,
        narration_artist: NarrationArtists,
        paragraph_delay: int = 500,
        sentence_delay: int = 0,
        model_path: str = None,
        model_config_path: str = None,
    ):
        self.paragraph_delay = paragraph_delay
        self.sentence_delay = sentence_delay
        self.model_path = model_path
        self.model_config_path = model_config_path
        self.narration_artist = narration_artist
        self._model = self._init_model()

    def _init_model(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        if all(
            [
                self.model_path is not None,
                self.model_config_path is not None,
            ]
        ):
            return TTS(
                model_path=self.model_path,
                config_path=self.model_config_path,
                progress_bar=False,
            ).to(device)

        return TTS(
            model_name=settings.default_xtts_model_name,
            vocoder_path=settings.default_xtts_vocoder_name,
            progress_bar=False,
        ).to(device)

    def chapter_iterator(self, text: str) -> tuple[str, int]:
        for text, delay in per_sentence_book_iterator(
            text=text,
            max_sentence_length=_CHARACTER_LIMIT_MAP[self.narration_artist.value.language],
            paragraph_delay=self.paragraph_delay,
            sentence_delay=self.sentence_delay,
        ):
            yield text, delay

    def narrate(self, chapter: Chapter) -> AudioSegment:
        segment = None
        delay = 0
        for text, next_delay in self.chapter_iterator(text=chapter.text):
            with NamedTemporaryFile('w+b', suffix='.wav') as wav:
                if is_wordless_line(text):
                    continue
                try:
                    self._model.tts_to_file(
                        text,
                        language=self.narration_artist.value.language.value,
                        file_path=wav.name,
                        speed=1.0,
                        speaker_wav=self.narration_artist.value.voice_sample_path,
                        split_sentences=True,
                    )
                except AssertionError as e:
                    raise UnableToNarrateException(
                        f'Unable to narrate line: {text}, '
                        f'book_id: {chapter.book_id}, '
                        f'chapter_number: {chapter.chapter_number}. Reason: {e}.',
                    )
                if segment is None:
                    segment = AudioSegment.from_wav(wav.name)
                    continue
                segment = segment.append(
                    AudioSegment.silent(duration=delay, frame_rate=segment.frame_rate),
                    crossfade=0,
                )
                segment = segment.append(AudioSegment.from_wav(wav.name), crossfade=0)
                delay = next_delay
        return segment
