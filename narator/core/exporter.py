from rich.progress import Progress, TextColumn, SpinnerColumn
from rich import print as rich_print
from narator.core.audio import apply_filters, convert_to_mp3, modify_mp3_metadata, concat_audio_fragments
from narator.storage.base import get_book, get_chapters


def export_chapters(start: int, step: int, book_id: int, cover_path: str = None):
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
            if not chapters:
                rich_print('[red]Chapter not found :(.')
                return
            file = concat_audio_fragments(*[c.audio.data for c in chapters], delay=3000)
            file = apply_filters(file)
            file = convert_to_mp3(file)
            file = modify_mp3_metadata(
                mp3_bytes=file,
                title=f'{chapters[0].chapter_number} - {chapters[-1].chapter_number}',
                artist=book.title,
                cover=open(cover_path, 'rb').read(),
            )
            file_name = f'{chapters[0].chapter_number} - {chapters[-1].chapter_number} - {book.title}.mp3'
            with open(file_name, 'wb') as result_file:
                result_file.write(file)
            _pointer += step
