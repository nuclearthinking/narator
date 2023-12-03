from tempfile import NamedTemporaryFile

import torch
from TTS.api import TTS
from rich.progress import Progress, TextColumn, SpinnerColumn

from narator.storage.base import get_next_chapter, save_dubbed_chapter
from narator.core.text_tools import prepare_sentences


def start_voiceover(book_id: int, start: int = 0):
    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        progress.add_task(description='[green]Loading model ...', total=None)
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = TTS(
            model_name='tts_models/multilingual/multi-dataset/xtts_v2',
            vocoder_path='vocoder_models/universal/libri-tts/fullband-melgan',
            progress_bar=False,
        ).to(device)

    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description='[green]Processing chapters ...', total=None)
        while chapter := get_next_chapter(book_id=book_id, chapter_from=start):
            progress.update(task_id, description=f'[green]Processing chapter {chapter.chapter_number} ...')
            text = prepare_sentences(chapter.text)
            with NamedTemporaryFile('w+b', suffix='.wav') as wav:
                model.tts_to_file(
                    text, language='en', file_path=wav.name, speed=1.15, speaker_wav='resources/chris_lutkin.wav'
                )
                wav.seek(0)
                save_dubbed_chapter(
                    chapter_id=chapter.id,
                    data=wav.read(),
                    book_id=book_id,
                )
