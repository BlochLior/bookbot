def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_character_count(text)
    sorted_dict_list = get_sorted_list_of_dicts(num_characters)
    print(f"---Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    printout(sorted_dict_list)
    print("--- End report ---")
    # herein i want to iterate the sorted alphabetic dictionary

def printout(sorted_list):
    for i in range(0, len(sorted_list)):
        char = sorted_list[i]["character"]
        counter = sorted_list[i]["counter"]
        print(f"The '{char}' character was found {counter} times")

def key_sort(item):
    return item["counter"]
    
def get_sorted_list_of_dicts(char_dict):
    symbolless = {}
    for char in char_dict:
        if char.isalpha():
            symbolless[char] = char_dict[char]
    dict_list = []
    for char in symbolless:
        counter = symbolless[char]
        dict_list.append({"character": char, "counter": counter})
    dict_list.sort(reverse=True, key=key_sort)
    return dict_list
    


def get_character_count(text):
    lowercase_text = text.lower() # i have now the entire text as lowercase
    char_count = {}
    for character in lowercase_text:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1


    return char_count
    


def get_num_words(text):
    word_count = text.split()
    return len(word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()