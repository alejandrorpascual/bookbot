def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def get_words_from_text(file_path: str) -> list[str]:
    txt = get_book_text(file_path)
    return txt.split()


def count_words(words: list[str]) -> int:
    return len(words)
