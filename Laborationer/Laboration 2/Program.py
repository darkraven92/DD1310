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
