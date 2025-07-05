import sys
from stats import get_num_words, get_num_chars

def get_book_text(filepath):
    ##Get book content_string

    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
        #do something with f (the file) here
    return file_contents

def main():
    if 1 == len(sys.argv):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    
    relative_path = sys.argv[1]
    # relative_path = "./books/frankenstein.txt"

    
    file_contents = get_book_text(relative_path)
    char_count = get_num_chars(file_contents)
    
    ##User Output
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", get_num_words(file_contents), "total words")
    print("--------- Character Count -------")

    sorted_dict = sorted(char_count, key=char_count.get, reverse=True)
    for index in sorted_dict:
        print(index + ":", char_count[index])

    print("============= END ===============")
    
    sys.exit(0)


main()