from stats import get_word_count, get_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_data = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(book_data)
    num_char = get_char_count(book_data)

    print(f"{num_words} words found in the document")
    print(num_char)


if __name__ == "__main__":
    main()
