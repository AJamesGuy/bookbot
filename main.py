from stats import count_words, count_symbols, sorted_counts
import sys

def get_book_text(fpath):
    with open(fpath) as f:
        content = f.read()
    return content
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("========BOOKBOT========)")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("-------- Word Count --------")
    text = get_book_text(sys.argv[1])
    count = count_words(text)
    print(f"Found {count} total words")
    print("-------- Character Count --------")
    counts = count_symbols(text)
    ordered = sorted_counts(counts)
    for dict in ordered:
        for k, v in dict.items():
            print(f'{k}: {v}')


main()