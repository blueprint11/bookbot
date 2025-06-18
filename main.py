import sys

def get_book_text(filepath):
    with open(filepath) as frankenstein:
        file_contents= frankenstein.read()
    return file_contents

def main():
    s=get_book_text(filepath=sys.argv[1])
    number=get_words(str=s)
    counts=no_of_time(text=s)
    res=sorted_dict(dictionary=counts)
    
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for item in res:
    
        ch=item["char"]
        nm=item["num"]
        print (f"{ch}: {nm}")
            
if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)    

from stats import no_of_time

from stats import get_words

from stats import sorted_dict
main()
    