#Uppgift 1: Bränsleförbrukning

def bransleforbrukning():

    p = float(input("Bilens körsträcka i km: "))
    fb = float(input("Hur mycket förbrukat bränsle i liter:"))


    bf = (100*fb)/p

    print("Bränsleförbrukningen för bilen är: ",round(bf, 3))

bransleforbrukning()