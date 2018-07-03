import math
import random


#Uppgift 1: For-satser och range

def convertToFah():

    for c in range(1,21):
        f = (c*9+160)/5
        print(f)

#convertToFah()

#Uppgift 2: Nästlade slingor

def nestedloop():
    rad = int(input("Ange antal rader:"))
    kol = int(input("Ange antal kolumner:"))
    i = 0

    while i <= rad:
        j = 0
        while j <= kol:
            if i + j == 0:
                print('{:4s}'.format(''), end='')
            elif i * j == 0:
                print('{:4d}'.format(i + j), end='')
            else:
                print('{:4d}'.format(i * j), end='')
            j = j + 1
        print()
        i = i + 1
#nestedloop()

#Uppgift 3: Slingor och listor

def dicegame():

    dice = int(input("Hur många tärningar behövs i spelet:"))
    throws = int(input("Hur många kast en spelare får:"))
    key = input(print("Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv a:"))
    counterd = 0
    countert = 0
    dicer = 0
    diceroll = []

    if key == "enter":
        while(countert < throws):
            countert += 1

            while(counterd < dice):
                counterd += 1
                dicer = random.randint(1,6)
                diceroll.append(dicer)
                print("Tärning",counterd,":",dicer)

        print("Är du inte nöjd kan du kasta, igen, vill du kasta igen?(j/n)")
        if key == "n":
            for x in diceroll:
                print(x)

    elif key == "a":
        quit()







dicegame()