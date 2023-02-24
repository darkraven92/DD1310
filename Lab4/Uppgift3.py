def kupering(word):
    """Konstruerar ordet som uppstår när de första bokstäverna i word
    flyttas till slutet."""
    return word[1:] + word[0]

def linsokkup(lista):
    """Söker igenom listan efter par av typen "alpin" och "pinal"
    eller andra par som kan konstrueras genom att flytta första
    bokstäverna på ett ord till slutet."""
    found_pairs = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if kupering(lista[i]) == lista[j] and kupering(lista[j]) == lista[i]:
                found_pairs.append((lista[i], lista[j]))
                print(lista[i], lista[j])
    return found_pairs

  with open("ordlistau.txt", encoding="utf-8") as f:
    ordlista = [line.strip() for line in f]
kuperade_par = linsokkup(ordlista)
