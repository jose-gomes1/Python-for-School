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

def main():
    funcao()

if __name__ == "__main__":
    main()