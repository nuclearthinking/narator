import re
from pathlib import Path

from narator.core.constants import CONFIG_FILE_NAME


def get_config_dir():
    path = Path.home() / CONFIG_FILE_NAME
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path


def parse_plain_text_to_chapters(content: str):
    chapters = {}
    for r in re.findall(r'Глава \d{1,2}', content):
        chapters[r] = content.index(r)
    keys = list(chapters.keys())
    values = list(chapters.values())

    for i, key in enumerate(keys):
        start = values[i]
        end = values[i + 1] if i + 1 < len(values) else len(content)
        chapters[key] = content[start:end]
    chapter_number = 1
    result = []
    for key, value in chapters.items():
        result.append(
            {
                'chapter_number': chapter_number,
                'text': value,
                'title': key,
            }
        )
        chapter_number += 1
    return result
