import sys
from stats import get_words_count, character_count, sort_char_counts

file = sys.argv

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    number = get_words_count(text)
    quantity = character_count(text)
    ordered_count = sort_char_counts(quantity)
    
    
    print(f"Found {number} total words")
    for entry in ordered_count:
        ch = entry["char"]
        num = entry["num"]

        # Skip non-alphabetical characters
        if not ch.isalpha():
            continue

        print(f"{ch}: {num}")
    
main()