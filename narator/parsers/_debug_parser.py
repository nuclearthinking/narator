
from narator.core.enums.narration_language import NarrationLanguage
from narator.parsers.lightnovelworld_parser import LightNovelWorldParser

parser = LightNovelWorldParser(debug=False)

parser.parse(
    start_url='https://www.lightnovelworld.com/novel/supreme-lord-i-can-extract-everything-1623/chapter-1',
    book_id=8,
    book_name='Supreme Lord: I can extract everything!',
    language=NarrationLanguage.en,
)
