def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_word_count(str):
    return len(str.split())


def main():
    num_words = get_word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
