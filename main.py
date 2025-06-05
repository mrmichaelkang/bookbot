from stats import get_word_count, get_char_count, generate_report_format


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    file_path = "books/frankenstein.txt"
    book_data = get_book_text(file_path)
    num_words = get_word_count(book_data)
    num_char = get_char_count(book_data)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    report = generate_report_format(num_char)

    for item in report:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
