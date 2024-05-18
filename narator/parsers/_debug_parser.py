from narator.core.enums.narration_language import NarrationLanguage
from narator.parsers.lightnovelworld_parser import LightNovelWorldParser

parser = LightNovelWorldParser(debug=False)

parser.parse(
    start_url='https://www.lightnovelworld.co/novel/the-martial-unity-1509/chapter-1-16060047',
    book_id=5,
    book_name='The Martial Unity',
    language=NarrationLanguage.en,
)
