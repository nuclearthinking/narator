import sys

from narator.audio_tools import concat_audio_fragments, clean_audio, convert_to_mp3, modify_mp3_metadata
from narator.storage import get_chapters

if __name__ == '__main__':
    while chapters := get_chapters(book_id=1, chapter_number=566, limit=10):
        chapters = [c for c in chapters if c.audio]
        if not chapters:
            sys.exit(0)
        result_file = concat_audio_fragments(*[c.audio.data for c in chapters])
        cleaned_file = clean_audio(result_file)
        mp3_file = convert_to_mp3(cleaned_file)
        modified_file = modify_mp3_metadata(
            mp3_file,
            f'{chapters[0].chapter_number} - {chapters[-1].chapter_number + 1}',
            'The Mech Touch',
        )
        file_name = f'{chapters[0].chapter_number} - {chapters[-1].chapter_number + 1} - The Mech Touch.mp3'
        with open(file_name, 'wb') as result_file:
            result_file.write(modified_file)
