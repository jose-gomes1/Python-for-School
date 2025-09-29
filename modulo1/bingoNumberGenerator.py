import random

random.seed()

a = 0
bingoNums = list(range(1, 101))

while a != "q":
    if not bingoNums:
        print("Acabaram os números")
        break

    chosen = random.choice(bingoNums)
    bingoNums.remove(chosen)
    print("Número:",chosen)

    a = input("Prima qualquer tecla para continuar ('q' para sair)").lower()
