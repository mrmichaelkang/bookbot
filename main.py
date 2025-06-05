from stats import get_word_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    num_words = get_word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
