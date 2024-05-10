import typing

if typing.TYPE_CHECKING:
    from narator.core.enums.narration_mode import NarrationMode
    from narator.core.narators.base_narrator import BaseNarrator
    from narator.core.enums.narration_artists import NarrationArtists


def get_narration_engine(
    narration_mode: NarrationMode,
    narration_artist: NarrationArtists = NarrationArtists.oleg_keinz,
) -> BaseNarrator:
    if narration_mode.coqui:
        from narator.core.narators.coqui_narrator import CoquiNarrator

        return CoquiNarrator(
            narration_artist=narration_artist,
        )
    else:
        from narator.core.narators.yandex_narrator import YandexNarrator

        return YandexNarrator(
            characters_limit=4900,
            paragraph_delay=1000,
            sentence_delay=0,
        )
