import sys

def sort_list(words):
    return sorted(words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, introduce una lista de palabras separadas por espacios.")
        sys.exit(1)

    palabras = sys.argv[1:]
    ordenadas = sort_list(palabras)

    print("Palabras ordenadas:")
    for palabra in ordenadas:
        print(palabra)
