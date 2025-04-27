from stats import get_words_from_text, count_words


def main():
    words_from_text = get_words_from_text("./books/frankenstein.txt")
    word_count = count_words(words_from_text)
    print(f"{word_count} words found in the document")


main()
