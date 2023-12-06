from tempfile import NamedTemporaryFile

import torch
from pydub import AudioSegment
from TTS.api import TTS
from rich.progress import Progress, TextColumn, SpinnerColumn

from narator.storage.base import get_next_chapter, save_dubbed_chapter
from narator.core.text_tools import book_iterator


def narrate(book_id: int, start: int = 0):
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

            segment = None
            delay = 0
            for line, next_delay in book_iterator(chapter.text, paragraph_delay=500):
                with NamedTemporaryFile('w+b', suffix='.wav') as wav:
                    model.tts_to_file(
                        line,
                        language='en',
                        file_path=wav.name,
                        speed=1.15,
                        speaker_wav='resources/neil_gaiman.wav',
                        split_sentences=False,
                    )

                    if segment is None:
                        segment = AudioSegment.from_wav(wav.name)
                    else:
                        segment = segment.append(
                            AudioSegment.silent(duration=delay, frame_rate=segment.frame_rate),
                            crossfade=0,
                        )
                        segment = segment.append(AudioSegment.from_wav(wav.name), crossfade=0)
                    delay = next_delay

            with NamedTemporaryFile('w+b', suffix='.wav') as tmp_wav:
                segment.export(tmp_wav.name, format='wav')
                save_dubbed_chapter(
                    chapter_id=chapter.id,
                    data=tmp_wav.read(),
                    book_id=book_id,
                )
