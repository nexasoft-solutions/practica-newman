import sys

def sort_list(words, remove_duplicates=False):
    if remove_duplicates:
        words = list(set(words))
    return sorted(words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter a list of words separated by spaces.")
        sys.exit(1)

    remove_duplicates = "--no-duplicates" in sys.argv

    words = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    sorted_words = sort_list(words, remove_duplicates)

    print("Sorted words:")
    for word in sorted_words:
        print(word)
