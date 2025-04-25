import sys
from stats import get_num_words, get_char_count, sort_char_count

def main():
    # Handle CLI arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found")
        sys.exit(1)
    
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_chars = sort_char_count(char_count)
    
    # Generate report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print all characters including non-alphabetical (removed .isalpha() filter)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")

def get_book_text(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    main()



    