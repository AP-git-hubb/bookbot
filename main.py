from stats import count_words, count_letters, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(p):
    with open(p) as f:
        return f.read()

def main():
    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(f"Found {word_count} total words")
    for d in sort_dict(letter_count):
        print(d["char"] + ": " + str(d["num"]))
    
    

main()