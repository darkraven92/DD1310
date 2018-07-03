#Uppgift 1: Bränsleförbrukning

def bransleforbrukning():

    p = float(input("Bilens körsträcka i km: "))
    fb = float(input("Hur mycket förbrukat bränsle i liter:"))


    bf = (100*fb)/p

    print("Bränsleförbrukningen för bilen är: ",round(bf, 3))

#bransleforbrukning()

#Uppgift 2: If-satser
def tabell():

    anv_input = float(input("Hur mycket väger paketet:"))
    if anv_input <= 2:
        pris = anv_input*30
        print("Det kommer att kosta",pris,"kr")
    elif anv_input > 2 and anv_input <=6:
        pris = anv_input*28
        print("Det kommer att kosta",pris,"kr")
    elif anv_input > 6 and anv_input <= 12:
        pris = anv_input*25
        print("Det kommer att kosta",pris,"kr")
    elif anv_input > 12:
        pris = anv_input*23
        print("Det kommer att kosta",pris,"kr")

#tabell()

#Uppgift 3: Slingor

# TODO Hitta felet med None
def slingor():
    antal_paket = int(input("Hur många paket vill du skicka:"))
    counter = 0
    summa_paket = 0

    while counter < antal_paket:
        counter += 1
        vikt = int(input(print("Ange vikt för paket",counter,":")))

        if vikt <= 2:
            pris = vikt*30
            summa_paket = summa_paket + pris
        elif vikt > 2 and vikt <= 6:
            pris = vikt*28
            summa_paket = summa_paket + pris
        elif vikt > 6 and vikt <= 12:
            pris = vikt*25
            summa_paket = summa_paket + pris
        elif vikt > 12:
            pris = vikt*23
            summa_paket = summa_paket + pris

    print("Det kommer att kosta",summa_paket,"kr")



slingor()
