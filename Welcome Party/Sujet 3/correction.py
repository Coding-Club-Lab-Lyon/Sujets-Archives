import random
n = random.randint(1,100)
var = 0

while var != n:
    var = int(input("Entrez un nombre : "))
    if var < n:
        print("Trop bas")
    if var > n:
        print("Trop haut")
print("Bien joué !")
