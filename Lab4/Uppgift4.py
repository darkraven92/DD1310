def binsok(lista, elem):
    """Returns True if the sorted list lista contains elem and False otherwise."""
    start = 0
    end = len(lista) - 1
    while start <= end:
        mid = (start + end) // 2
        if lista[mid] == elem:
            return True
        elif lista[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1
    return False

# Anropa funktionen binsok för varje inmatat ord och skriv ut resultatet
with open("word3.txt", "r", encoding="utf-8") as fil:
    ordlista = fil.read().split()

while True:
    sokord = input("Ditt ord: ")
    if binsok(ordlista, sokord):
        print(sokord, "finns")
    else:
        print(sokord, "finns inte")
