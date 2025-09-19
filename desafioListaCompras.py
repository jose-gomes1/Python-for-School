compras = ["pão", "leite", "maçãs"]

a = input("O que deseja comprar? ")
compras.append(a)
b = ", ".join(compras)
num = len(compras)

print(f"Aqui está a lista de compras, tem {num} items: ")
print(b)