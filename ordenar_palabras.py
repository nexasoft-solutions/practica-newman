import sys

def sort_list(words, eliminar_duplicados=False):
    if eliminar_duplicados:
        words = list(set(words))
    return sorted(words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, introduce una lista de palabras separadas por espacios.")
        sys.exit(1)

    # Detecta si se pasó la opción --sin-duplicados
    eliminar_duplicados = "--sin-duplicados" in sys.argv

    # Filtra las palabras, eliminando argumentos con --
    palabras = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    ordenadas = sort_list(palabras, eliminar_duplicados)

    print("Palabras ordenadas:")
    for palabra in ordenadas:
        print(palabra)
