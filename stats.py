def get_book_wordcount(file_path):
    story = get_book_text(file_path)
    words = story.split()
    return len(words)

def sort_on(dict):
    return dict['num']

def get_sorted_character_count(file_path):
    unsorted_dict = get_book_character_count(file_path)
    toSort = []
    for key in unsorted_dict:
        toSort.append({'char' : key, 'num' : unsorted_dict[key]})
    toSort.sort(key=sort_on, reverse=True)
    return toSort

def get_book_character_count(file_path):
    story = get_book_text(file_path)
    returnDict = dict()
    for char in story:
        lowerchar = char.lower()
        if lowerchar in returnDict:
            returnDict[lowerchar] += 1
        else:
            returnDict[lowerchar] = 1
        
    return returnDict

def get_book_text(file_path):
    # return "blah : " + file_path
    with open(file_path, encoding='utf-8') as f:
        return f.read()