def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_num_chars(book_text):
    counters = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in counters:
            counters[lower_char] = 0
        counters[lower_char] += 1
    return counters


def sort_on(item):
    return item["num"]


def get_list_of_dicts(num_chars):
    new_list = []
    for char in num_chars:
        new_list.append({"char": char, "num": num_chars[char]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
