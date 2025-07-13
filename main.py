import sys
from stats import get_book_wordcount
from stats import get_book_character_count
from stats import get_sorted_character_count
def main():


    bookDirectory = ""
    if len(sys.argv) > 1:
        bookDirectory = sys.argv[1]
    else:
        print("Error no book selected, Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {bookDirectory}...")

    print("----------- Word Count ----------")
    wordCount = get_book_wordcount(bookDirectory)    
    


    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    # unsorted_char_dict = get_book_character_count(bookDirectory)    

    # #unsorted list
    # for key in unsorted_char_dict:
    #     print(f"'{key}': {unsorted_char_dict[key]}")


    # print("-----Sorted:------ ")
    sorted_dict = get_sorted_character_count(bookDirectory)


    for sorted in sorted_dict:
        print(f"{sorted['char']}: {sorted['num']}")
    print("Main Done")



main()