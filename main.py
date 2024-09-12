def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    nun_words = count_words(text)
    num_character = count_characters(text)
    sorted_alpha = is_alpha(num_character)
    print(f"--- Begin report of {book_path} ---")
    print(f"{nun_words} words found in the document")
    print()
    for x in sorted_alpha:
        print(f"The '{x[0]}' character was found {x[1]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    freq = {}
    for c in text:
        lowered = c.lower()
        if lowered in freq:
            freq[lowered] += 1
        else:
            freq[lowered] = 1
    return freq

def is_alpha(character):
    num_alpha = {}
    for c in character:
        if c.isalpha() == True:
            num_alpha[c] = character[c]
    sorted_alpha = sorted(num_alpha.items(), key=lambda x:x[1], reverse=True)
    return sorted_alpha

main()