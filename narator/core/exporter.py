from rich.progress import Progress, TextColumn, SpinnerColumn

from narator.storage.base import get_book, get_chapters
from narator.core.audio_tools import (
    apply_filters,
    convert_to_mp3,
    add_mp3_cover_art,
    modify_mp3_metadata,
    concat_audio_fragments,
)


def export_chapters(start: int, step: int, book_id: int):
    _pointer = start
    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description='[green]Exporting chapters ...', total=None)
        book = get_book(book_id=book_id)
        while chapters := get_chapters(book_id=book_id, chapter_number=_pointer, limit=step):
            progress.update(
                task_id,
                description=f'[green]Exporting chapters {chapters[0].chapter_number} - {chapters[-1].chapter_number} ...',
            )
            chapters = [c for c in chapters if c.audio]
            if not chapters or len(chapters) < step:
                return
            file = concat_audio_fragments(*[c.audio.data for c in chapters], delay=1000)
            file = apply_filters(file)
            file = convert_to_mp3(file)
            file = modify_mp3_metadata(
                mp3_bytes=file,
                title=f'{chapters[0].chapter_number} - {chapters[-1].chapter_number}',
                artist=book.title,
            )
            file = add_mp3_cover_art(
                mp3_bytes=file,
                cover_bytes=open('resources/the_mech_touch_02.jpg', 'rb').read(),
            )
            file_name = f'{chapters[0].chapter_number} - {chapters[-1].chapter_number} - {book.title}.mp3'
            with open(file_name, 'wb') as result_file:
                result_file.write(file)
            _pointer += step
