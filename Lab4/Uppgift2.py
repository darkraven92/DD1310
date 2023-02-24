def linsok(lista, elem):
    for x in lista:
        if x == elem:
            return True
    return False

  def main():
    # Läs in ordlistan
    with open('ordlista.txt', 'r') as f:
        ordlista = [line.strip() for line in f]

    while True:
        # Läs in sökordet
        sokord = input('Ditt ord: ')

        # Anropa linsok för att söka efter ordet i listan
        if linsok(ordlista, sokord):
            print(sokord, 'finns')
        else:
            print(sokord, 'finns inte')
