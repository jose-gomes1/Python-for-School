import random

random.seed()

a = 0
bingoNums = list(range(1, 101))

def generatorFunction():
    while a != "q":
        if not bingoNums:
            print("Acabaram os números")
            print("B I N G O !")
            break

        chosen = random.choice(bingoNums)
        bingoNums.remove(chosen)
        print("Número:",chosen)

        a = input("Prima qualquer tecla para continuar ('q' para sair)").lower()

def generateCard():
    numCards = random.sample((1, 101), 8)
    card = [numCards[0], numCards[1], numCards[2],
            numCards[3], "Free Space", numCards[4],
            numCards[5], numCards[6], numCards[7]]
    return card

def player():
    b = input(int("Quantos cartões quer gerar? "))
    while i in b:
        card[i] = generateCard()
        
