import sys

from narator.storage.base import get_chapters
from narator.core.audio_tools import clean_audio, convert_to_mp3, modify_mp3_metadata, concat_audio_fragments

if __name__ == '__main__':
    start = 565
    step = 5
    while chapters := get_chapters(book_id=1, chapter_number=start, limit=step):
        chapters = [c for c in chapters if c.audio]
        if not chapters:
            sys.exit(0)
        result_file = concat_audio_fragments(*[c.audio.data for c in chapters])
        cleaned_file = clean_audio(result_file)
        mp3_file = convert_to_mp3(cleaned_file)
        modified_file = modify_mp3_metadata(
            mp3_file,
            f'{chapters[0].chapter_number} - {chapters[-1].chapter_number}',
            'The Mech Touch',
        )
        file_name = f'{chapters[0].chapter_number} - {chapters[-1].chapter_number} - The Mech Touch.mp3'
        with open(file_name, 'wb') as result_file:
            result_file.write(modified_file)
        start += step
