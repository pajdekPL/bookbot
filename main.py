from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counter = get_characters_counter(text)   
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    for item in counter.most_common():
        if not item[0].isalpha():
            continue
        print(f"The '{item[0]}' character was found {item[1]} times")
        
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_characters_counter(text):
    return Counter(text.lower())
main()