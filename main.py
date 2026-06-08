import sys
from stats import count_words,count_characters,sort_dictionary,summarize_text
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def menu(text):
     while True:
        print("""Select 1 to summarize the content of the book provided
        Select 2 to get the count of each character used in the book
        Select 3 to exit the program""")
        choice=input("Enter your choice:")
        if choice=='3':
            sys.exit(0)
        elif choice=='2':
            count=count_words(text)
            count_char=count_characters(text)
            print("============ BOOKBOT ============\n"
f"Analyzing book found at {sys.argv[1]}...\n"
"----------- Word Count ----------\n"
f"Found {count} total words\n"
"--------- Character Count -------")
            sorted_list=sort_dictionary(count_char)
            for k in sorted_list:
                if k["char"].isalpha():
                    print(f"{k['char']}: {k['num']}")
        elif choice=='1':
            summary=summarize_text(text)
            print(summary)
        else:
            print("Invalid Choice")

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    menu(book_text) 
main()
