import re
import textwrap


def split_line(line: str, limit=250) -> list[str]:
    pattern = r'(?<=[.!?])( )(?!\s*$|\"|$|\n)'
    matches = re.split(pattern, line)
    stripped_sentences = [e.strip() for e in matches]
    filtered_sentences = list(filter(bool, stripped_sentences))
    result = []

    for sentence in filtered_sentences:
        if len(sentence) < limit:
            result.append(sentence)
        else:
            result.extend(textwrap.wrap(sentence, limit))

    return result


def _is_meaningless_line(line: str) -> bool:
    return line.strip() == '' or bool(re.match(r'^[\W_]*$', line))


def prepare_sentences(input_text: str) -> str:
    sentences = []
    for line in filter(bool, input_text.split('\n')):
        if _is_meaningless_line(line):
            continue
        if len(line) < 250:
            sentences.append(line)
            continue

        sentences.extend(split_line(line, 250))

    return '\n'.join(sentences)
