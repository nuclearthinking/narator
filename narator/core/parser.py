from narator.core.enums.narration_language import NarrationLanguage
from narator.core.enums.parser_mode import ParserMode
from narator.parsers.base_parser import BaseParser
from narator.parsers.fb2_parser import Fb2Parser
from narator.parsers.readnovelfull_parser import ReadNovelFullParser


def get_parser(parser_mode: ParserMode) -> BaseParser:
    if parser_mode == ParserMode.fb2:
        return Fb2Parser()
    if parser_mode == ParserMode.readnovelfull:
        return ReadNovelFullParser()


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
