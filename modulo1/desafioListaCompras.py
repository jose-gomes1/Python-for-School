def funcao():
    compras = []

    cancelar = ["cancel", "exit", "cancelar", "sair"]

    while True:
        a = input("O que deseja comprar? ")
        if a.lower() in cancelar:
            break
        elif a:
            if a.lower() in compras:
                print(f"{a} já está na lista")
            else:
                compras.append(a.lower())

    b = ", ".join(compras)
    num = len(compras)

    print(f"Aqui está a lista de compras, tem {num} items: ")
    print(b)

# listas
def listas():
    frutas = ["maçã", "banana", "laranja"]
    frutasN = frutas.copy()
    print(frutas)
    print(frutasN)

# tuples
def tuples():
    carros = ("BMW", "Audi", "Mercedes")
    (marca1, marca2, marca3) = carros # unpacking: relaciona valores com chaves
    print(marca1)
    marca2 = "Fiat"
    print(marca2)
    print(carros[1])


tuples()