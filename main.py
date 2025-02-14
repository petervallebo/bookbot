def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_list = get_characters(text)
    print_report(num_words, char_list)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_characters(text):
    text_lower = text.lower()
    count_char = {}
    
    # Only count alphabetic characters

    for characters in text_lower:
        if characters.isalpha():
            if characters not in count_char:
                count_char[characters] = 0
            count_char[characters] += 1
    

    # Convert to list of dictionaries

    char_list = []
    for char, count in count_char.items():
        char_list.append({"char": char, "num": count})

    return char_list

def sort_on(dict):
    return dict["num"]


# Print function
def print_report(num_words, char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    # Sort the list before printing
    char_list.sort(reverse=True, key=sort_on)

    # print each character count

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report --- ")


main()


#path_to_file = "books/frankenstein.txt"
#
#def main(path_to_file):
#    with open(path_to_file) as f:
#        file_contents = f.read()
#    return file_contents
#
#file_contents = main(path_to_file)
#
#def word_count(file_contents):
#    words = file_contents.split()
#    word_count = len(words)
#    print(word_count)
#
#
#word_count(file_contents)