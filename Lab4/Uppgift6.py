# Funktion för binärsökning
def binsok(lista, elem):
    """Returns True if elem is in the sorted list lista, False otherwise"""
    left, right = 0, len(lista)-1
    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == elem:
            return True
        elif lista[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Funktion för att läsa in ordlista
def read_words(filename):
    """Reads a file with one word per line and returns a list of the words"""
    with open(filename, encoding="utf-8") as file:
        words = file.read().splitlines()
    return words

# Läs in ordlistan
words = read_words("ordlista.txt")

# Funktion för att hitta ord med "alpin" och "pinal" med hjälp av binärsökning
def binsokkup():
    for word in words:
        if binsok(words, "alpin"+word) and binsok(words, "pinal"+word):
            print(word)

# Testprogram med binärsökning
def test_binsok():
    while True:
        search_word = input("Ditt ord: ")
        if binsok(words, search_word):
            print(search_word, "finns")
        else:
            print(search_word, "finns inte")

# Kör testprogrammet med binärsökning
test_binsok()

# Testa funktionen för att hitta ord med "alpin" och "pinal"
binsokkup()
