from tempfile import NamedTemporaryFile

import torch
from TTS.api import TTS

from narator.storage import get_chapter, save_dubbed_chapter

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2', progress_bar=True).to(device)


def split_long_line(character: str, index: int, line: str, _result: list) -> list[str]:
    if len(line) < 250:
        return [line]
    _result = _result if _result else []
    split_index = line.rfind(' ', 0, 250)

    first_part = line[:split_index]
    second_part = line[split_index + 1:]
    _result.append(first_part)

    if len(second_part) > 250:
        return split_long_line(character, index, second_part, _result)
    else:
        _result.append(second_part)
        return _result


def start_dubbing():
    start = 566
    while chapter := get_chapter(chapter_number=start, book_id=1):
        if chapter.audio is not None:
            start += 1
            continue
        sentences = []
        for line in filter(bool, chapter.text.split('\n')):
            if len(line) < 250:
                sentences.append(line)
                continue
            if '. ' in line:
                sentences.extend(line.split('. '))
                continue
            else:
                sentences.extend(split_long_line(' ', 250, line, []))
                continue
        text = '\n'.join(sentences)

        with NamedTemporaryFile('w+b', suffix='.wav') as wav:
            model.tts_to_file(text, language='en', file_path=wav.name, speaker_wav='neil_gaiman.wav')
            wav.seek(0)
            save_dubbed_chapter(
                chapter_id=chapter.id,
                data=wav.read(),
            )

        start += 1


if __name__ == '__main__':
    start_dubbing()
