from tempfile import NamedTemporaryFile

from rich.progress import Progress, TextColumn, SpinnerColumn

from narator.core.narators.yandex_narrator import YandexNarrator
from narator.storage.base import get_next_chapter, save_narrated_chapter
from narator.core.enums.narration_artists import NarrationArtists
from narator.core.narators.coqui_narrator import CoquiNarrator


def narrate(
    book_id: int,
    start: int = 0,
):
    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        progress.add_task(description='[green]Loading model ...', total=None)
        narrator = CoquiNarrator(
            narration_artist=NarrationArtists.oleg_keinz,
        )

    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description='[green]Processing chapters ...', total=None)
        while chapter := get_next_chapter(book_id=book_id, chapter_from=start):
            progress.update(task_id, description=f'[green]Processing chapter {chapter.chapter_number} ...')
            narrated_chapter = narrator.narrate(chapter)
            with NamedTemporaryFile('w+b', suffix='.wav') as tmp_wav:
                narrated_chapter.export(tmp_wav.name, format='wav')
                save_narrated_chapter(
                    chapter_id=chapter.id,
                    data=tmp_wav.read(),
                    book_id=book_id,
                )


def narrate_y(
    book_id: int,
    start: int = 0,
):
    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        progress.add_task(description='[green]Loading model ...', total=None)
        narrator = YandexNarrator()

    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description='[green]Processing chapters ...', total=None)
        while chapter := get_next_chapter(book_id=book_id, chapter_from=start):
            progress.update(task_id, description=f'[green]Processing chapter {chapter.chapter_number} ...')
            narrated_chapter = narrator.narrate(chapter)
            with NamedTemporaryFile('w+b', suffix='.wav') as tmp_wav:
                narrated_chapter.export(tmp_wav.name, format='wav')
                save_narrated_chapter(
                    chapter_id=chapter.id,
                    data=tmp_wav.read(),
                    book_id=book_id,
                )
