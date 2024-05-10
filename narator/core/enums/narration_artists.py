from enum import Enum

from narator.core.entities.artists import NarrationArtist
from narator.core.enums.narration_language import NarrationLanguage


class NarrationArtists(Enum):
    chris_lutkin = NarrationArtist(
        name='Chris Lutkin',
        language=NarrationLanguage.en,
        voice_sample_path='resources/chris_lutkin.wav',
    )
    neil_gaiman = NarrationArtist(
        name='Neil Gaiman',
        language=NarrationLanguage.en,
        voice_sample_path='resources/neil_gaiman.wav',
    )
    oleg_keinz = NarrationArtist(
        name='Oleg Keinz',
        language=NarrationLanguage.ru,
        voice_sample_path='resources/oleg_keinz.mp3',
    )
