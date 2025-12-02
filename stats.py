def get_words_count(text):
    words = text.split()
    count = len(words)
    return count

def character_count(text: str) -> dict:
    text = text.lower()
    count = {}

    for char in text:
        count[char] = count.get(char, 0) + 1

    return count

def sort_char_counts(char_dict: dict) -> list:
    result = [{"char": c, "num": n} for c, n in char_dict.items()]

    # Helper function for sorting using the "num" key
    def get_num(entry):
        return entry["num"]

    # Sort list using helper function, reverse=True for greatest to least
    result.sort(key=get_num, reverse=True)

    return result

    