import sys
from stats import get_num_words, get_count_chars, get_sorted_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    text = get_book_text(sys.argv[1])
    words = get_num_words(text)
    chars = get_count_chars(text)
    report = get_sorted_report(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for line in report:
        print(f"{line["char"]}: {line["num"]} ")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()