from stats import count_unique_chars, get_book_text, get_words_from_text, count_words


def main():
    text = get_book_text("./books/frankenstein.txt")
    words = get_words_from_text(text)
    word_count = count_words(words)
    unique_chars = count_unique_chars(text)
    print(f"{word_count} words found in the document")
    print(unique_chars)


main()
