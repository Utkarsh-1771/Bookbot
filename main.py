import sys
from stats import count_words,count_characters,sort_dictionary
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    count=count_words(book_text)
    count_char=count_characters(book_text)

    print("============ BOOKBOT ============\n"
"Analyzing book found at books/frankenstein.txt...\n"
"----------- Word Count ----------\n"
"Found",count,"total words\n"
"--------- Character Count -------")
    sorted_list=sort_dictionary(count_char)
    for k in sorted_list:
        if k["char"].isalpha():
            print(f"{k['char']}: {k['num']}")
main()
