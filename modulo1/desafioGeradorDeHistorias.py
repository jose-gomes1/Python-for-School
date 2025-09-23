# desafio sugerido por IA

print("Olá! Bem-vindo(a), ao gerador de histórias. Que tal começarmos com algo simples?")
num = input("Quantas histórias deseja gerar? ")
historias = 0

while historias < int(num):
    nome = input("Qual é o nome da sua personagem? ")
    local = input("Qual o local que está tal personagem? ")
    acontecimento = input("O que aconteceu? ")
    item = input(str("Estaria tal personagem com um item específico que seria importante à história? "))


    if item.lower() == "sim":
        objeto = input("Qual seria o tal item? ")
        print(f"{nome} foi até {local} com {objeto} e acabou por {acontecimento}")
    else:
        print(f"{nome} foi até {local} e acabou por {acontecimento}")
    historias += 1