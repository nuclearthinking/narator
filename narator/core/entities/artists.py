from dataclasses import dataclass

from narator.core.enums.narration_language import NarrationLanguage


@dataclass
class NarrationArtist:
    name: str
    language: NarrationLanguage
    voice_sample_path: str
