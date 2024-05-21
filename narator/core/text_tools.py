import re
import textwrap


def split_line(line: str, limit=250) -> list[str]:
    line = line.strip()
    pattern = r'(?<=[.!?\"])( )((?!\s*$|\"|$|\n)|(?=\"))'
    matches = re.split(pattern, line)
    stripped_sentences = [e.strip() for e in matches]
    filtered_sentences = filter(bool, stripped_sentences)
    result = []

    for sentence in filtered_sentences:
        if len(sentence) <= limit:
            result.append(sentence)
        else:
            result.extend(textwrap.wrap(sentence, limit))

    return [s.strip() for s in result]


def is_wordless_line(line: str) -> bool:
    return line.strip() == '' or bool(re.match(r'^[\W_]*$', line))


def per_sentence_book_iterator(
    text: str,
    max_sentence_length: int = 250,
    paragraph_delay: int = 1000,
    sentence_delay: int = 0,
) -> tuple[str, int]:
    for text, delay in _per_sentence_book_iterator(
        text,
        max_sentence_length=max_sentence_length,
        paragraph_delay=paragraph_delay,
        sentence_delay=sentence_delay,
    ):
        text = preprocess_sentence(text)
        yield text, delay


def _per_sentence_book_iterator(
    text: str,
    max_sentence_length: int = 250,
    paragraph_delay: int = 1000,
    sentence_delay: int = 0,
) -> tuple[str, int]:
    paragraphs = text.split('\n')
    paragraphs = filter(bool, paragraphs)
    for line in paragraphs:
        line = line.strip()
        if len(line) <= max_sentence_length:
            yield line, paragraph_delay
            continue

        sentences = split_line(line, max_sentence_length)
        line = ''
        while sentences:
            new_line, *sentences = sentences
            if not line:
                line = new_line
                continue
            if len((line + ' ' + new_line).strip()) <= max_sentence_length:
                line = (line + ' ' + new_line).strip()
                if not sentences:
                    yield line.strip(), paragraph_delay
                continue
            else:
                yield line.strip(), sentence_delay
                line = new_line
                if not sentences:
                    yield line.strip(), paragraph_delay


def characters_limited_book_iterator(
    text,
    characters_limit=4900,
    paragraph_delay=1000,
    sentence_delay=0,
) -> tuple[str, int]:
    for text, delay in _characters_limited_book_iterator(
        text,
        characters_limit=characters_limit,
        paragraph_delay=paragraph_delay,
        sentence_delay=sentence_delay,
    ):
        text = preprocess_sentence(text)
        yield text, delay


def _characters_limited_book_iterator(
    text,
    characters_limit=4900,
    paragraph_delay=1000,
    sentence_delay=0,
) -> tuple[str, int]:
    lines = text.split('\n')
    lines = filter(bool, lines)

    result = ''

    while lines:
        next_line, *lines = lines

        if not result:
            result = next_line + '\n'
            continue

        if len(result + next_line) > characters_limit:
            yield result, paragraph_delay
            result = ''
            if len(next_line) == characters_limit:
                yield next_line, paragraph_delay
                continue
            if len(next_line) > characters_limit:
                sentences = split_sentences(next_line, characters_limit)
                if len(sentences) == 1:
                    yield next_line, paragraph_delay
                    continue
                *sentences, last_sentence = sentences
                for sentence in sentences:
                    yield sentence, sentence_delay
                result = last_sentence + '\n'
                continue
        else:
            result += next_line + '\n'
            if not lines:
                yield result, paragraph_delay


def split_sentences(text: str, characters_length: int) -> list[str]:
    if len(text) <= characters_length:
        return [text]
    sentences = split_line(text, characters_length)
    result = []
    line = ''
    for sentence in sentences:
        if len(line + ' ' + sentence) <= characters_length:
            line += ' ' + sentence
        else:
            result.append(line.strip())
            line = sentence
    return result


def correct_sentence_endings(text: str) -> str:
    endings_map = {
        re.compile(r'\w\."'): ('."', '".'),
        re.compile(r"\w\.'"): (".'", "'."),
    }
    result = []
    for word in text.split():
        for pattern, (old, new) in endings_map.items():
            if pattern.search(word):
                word = word.replace(old, new)
                break
        result.append(word)
    return ' '.join(result)


def replace_characters(text: str):
    char_map = {
        '’': "'",
        '‘': "'",
        '“': '"',
        '”': '"',
    }
    for char, replacement in char_map.items():
        text = text.replace(char, replacement)
    return text


def preprocess_sentence(text: str) -> str:
    text = replace_characters(text)
    text = correct_sentence_endings(text)
    return text
