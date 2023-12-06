import re
import textwrap


def split_line(line: str, limit=250) -> list[str]:
    line = line.strip()
    pattern = r'(?<=[.!?\"])( )((?!\s*$|\"|$|\n)|(?=\"))'
    matches = re.split(pattern, line)
    stripped_sentences = [e.strip() for e in matches]
    filtered_sentences = list(filter(bool, stripped_sentences))
    result = []

    for sentence in filtered_sentences:
        if len(sentence) <= limit:
            result.append(sentence)
        else:
            result.extend(textwrap.wrap(sentence, limit))

    return [s.strip() for s in result]


def _is_meaningless_line(line: str) -> bool:
    return line.strip() == '' or bool(re.match(r'^[\W_]*$', line))


def book_iterator(
    text: str,
    char_limit: int = 250,
    paragraph_delay: int = 1000,
    sentence_delay: int = 0,
) -> tuple[str, int]:
    paragraphs = text.split('\n')
    paragraphs = filter(bool, paragraphs)
    for line in paragraphs:
        line = line.strip()
        if len(line) <= char_limit:
            yield line, paragraph_delay
            continue

        sentences = split_line(line, char_limit)
        line = ''
        while sentences:
            new_line, *sentences = sentences
            if not line:
                line = new_line
                continue
            if len((line + ' ' + new_line).strip()) <= char_limit:
                line = (line + ' ' + new_line).strip()
                if not sentences:
                    yield line.strip(), paragraph_delay
                continue
            else:
                yield line.strip(), sentence_delay
                line = new_line
                if not sentences:
                    yield line.strip(), paragraph_delay
