import sys

from stats import get_num_words, get_num_chars, get_list_of_dicts


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_filepath = sys.argv[1]
    print(f"Analizing book found at {book_filepath}")
    text = get_book_text(book_filepath)
    text_length = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {text_length} total words")
    num_chars = get_num_chars(text)
    print("--------- Character Count -------")
    for d in get_list_of_dicts(num_chars):
        if not d["char"].isalpha():
            continue
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
