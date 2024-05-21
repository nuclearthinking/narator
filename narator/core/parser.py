from narator.parsers.fb2_parser import Fb2Parser
from narator.parsers.base_parser import BaseParser
from narator.core.enums.parser_mode import ParserMode
from narator.parsers.readnovelfull_parser import ReadNovelFullParser
from narator.core.enums.narration_language import NarrationLanguage
from narator.parsers.lightnovelworld_parser import LightNovelWorldParser

_parser_mapping = {
    ParserMode.fb2: Fb2Parser,
    ParserMode.readnovelfull: ReadNovelFullParser,
    ParserMode.lightnovelworld: LightNovelWorldParser,
}


def get_parser(parser_mode: ParserMode) -> BaseParser:
    cls = _parser_mapping.get(parser_mode)
    if not cls:
        raise ValueError(f'Parser {parser_mode} not found')
    return cls()


def parse(
    mode: ParserMode,
    start_url: str,
    book_name: str,
    book_id: int,
    language: NarrationLanguage,
):
    parser = get_parser(mode)
    parser.parse(
        start_url=start_url,
        book_id=book_id,
        book_name=book_name,
        language=language,
    )
