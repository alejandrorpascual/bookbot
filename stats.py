from typing_extensions import Dict


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def get_words_from_text(txt: str) -> list[str]:
    return txt.split()


def count_words(words: list[str]) -> int:
    return len(words)


def count_unique_chars(text: str) -> Dict[str, int]:
    char_counts: Dict[str, int] = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts
