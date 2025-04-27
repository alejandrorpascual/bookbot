from typing import Dict, List, TypedDict
import re


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


CharCount = TypedDict("CharCount", {"char": str, "num": int})


def sort_on(dict: CharCount):
    return dict["num"]


def sorted_list_of_dicts(dict: Dict[str, int]) -> List[CharCount]:
    array_of_dict = [CharCount(char=key, num=value) for key, value in dict.items()]

    array_of_dict.sort(reverse=True, key=sort_on)
    return array_of_dict


def reporting_count(stats: List[CharCount]):
    count_report = [
        f"{item['char']}: {item['num']}"
        for item in stats
        if not re.search(r"\W", item["char"])
    ]

    return "\n".join(count_report)


def heading(title: str):
    return f"============ {title.upper().strip()} ============"


def separator(title: str):
    return f"----------- {title.capitalize().strip()} ----------"


def execute_main(file_path: str):
    text = get_book_text(file_path)
    word_count = count_words(get_words_from_text(text))
    count_report = reporting_count(sorted_list_of_dicts(count_unique_chars(text)))

    print(heading("bookbot"))
    print(f"Analyzing book found at {file_path}...")
    print(separator("Word Count"))
    print(f"Found {word_count} total words")
    print(separator("Character Count"))
    print(count_report)
    print(heading("end"))
