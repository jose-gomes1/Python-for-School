import random

random.seed()

bingoNums = list(range(1, 101))

def generatorFunction():
    a = 0
    while a != "q":
        if not bingoNums:
            print("Acabaram os números")
            print("B I N G O !")
            break

        chosen = random.choice(bingoNums)
        bingoNums.remove(chosen)
        print("Número:",chosen)

        a = input("Prima qualquer tecla para continuar ('q' para sair) ").lower()

def generateCard():
    numCards = random.sample(range(1, 101), 8)
    card = [[numCards[0], numCards[1], numCards[2]],
            [numCards[3], "X", numCards[4]],
            [numCards[5], numCards[6], numCards[7]]]
    
    return card

def player():
    b = int(input("Quantos cartões quer gerar? "))
    for i in range(b):
        cartao = generateCard()
        print(f"Cartão {i+1}:")
        for row in cartao:
            for item in row:
                print(item, end=" ")
            print()

def start():
    style = int(input("É jogador (1) ou gerador (2)? "))
    match style:
        case 1:
            player()
        case 2:
            generatorFunction()
        case _:
            print("Caractér inválido")
            return
        

if __name__ == "__main__":
    start()
