def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_file(book_path)

    print(f"--- Begin report of {book_path} ---")
    words_count = count_words(file_contents)
    print(f"{words_count} words found in the document")
    print("\n")
    letters_dict = count_letters(file_contents)
    letters_list = list(letters_dict.values())
    letters_list.sort(reverse=True)

    for num in letters_list:
        for k, v in letters_dict.items():
            if v == num and k.isalpha():
                print(f"The '{k}' character was found {num} times")
                break

    print("--- End report ---")


def count_words(str):
    words = str.split()
    return len(words)


def count_letters(str):
    letters = {}
    for c in str:
        lower_chr = c.lower()
        if lower_chr in letters:
            letters[lower_chr] += 1
        else:
            letters[lower_chr] = 0

    return letters


def read_file(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents


main()
