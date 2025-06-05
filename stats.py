def get_word_count(str):
    return len(str.split())


def get_char_count(str):
    char_dict = {}

    for char in str.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict
