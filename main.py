from stats import get_num_words, get_count_chars, get_sorted_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    text = get_book_text("./books/frankenstein.txt")
    words = get_num_words(text)
    chars = get_count_chars(text)
    report = get_sorted_report(chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for line in report:
        print(f"{line["char"]}: {line["num"]} ")
    print("============= END ===============")

main()