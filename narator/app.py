import torch
from TTS.api import TTS

from narator.storage import get_chapter

device = "cuda" if torch.cuda.is_available() else "cpu"

model = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2', progress_bar=True).to(device)

start = 550


def split_long_line(character: str, index: int, line: str, _result: list) -> list[str]:
    if len(line) < 250:
        return [line]
    _result = _result if _result else []
    split_index = line.rfind(" ", 0, 250)

    first_part = line[:split_index]
    second_part = line[split_index + 1:]
    _result.append(first_part)

    if len(second_part) > 250:
        return split_long_line(character, index, second_part, _result)
    else:
        _result.append(second_part)
        return _result


while chapter := get_chapter(chapter_number=start, book_id=1):
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

    model.tts_to_file(text, language='en', speaker_wav='neil_gaiman.wav', file_path=f'{chapter.chapter_number}.wav')
    start += 1
