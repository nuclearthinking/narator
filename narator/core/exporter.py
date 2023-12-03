from rich.progress import Progress, TextColumn, SpinnerColumn

from narator.storage.base import get_book, get_chapters
from narator.core.audio_tools import clean_audio, convert_to_mp3, modify_mp3_metadata, concat_audio_fragments


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
            result_file = concat_audio_fragments(*[c.audio.data for c in chapters])
            cleaned_file = clean_audio(result_file)
            mp3_file = convert_to_mp3(cleaned_file)
            modified_file = modify_mp3_metadata(
                mp3_file,
                f'{chapters[0].chapter_number} - {chapters[-1].chapter_number}',
                book.title,
            )
            file_name = f'{chapters[0].chapter_number} - {chapters[-1].chapter_number} - {book.title}.mp3'
            with open(file_name, 'wb') as result_file:
                result_file.write(modified_file)
            _pointer += step
