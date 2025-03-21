from stats import get_num_words
from stats import get_char_count
from stats import chars_dict_to_sorted_list
import sys

def check_for_input():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]

def get_book_text(filepath):
        with open(filepath) as f:
                file_contents = f.read()
        return file_contents

def main():
    filepath = check_for_input()
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    character_counts = get_char_count(book_text)
    sorted_chars = chars_dict_to_sorted_list(character_counts)
    
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
