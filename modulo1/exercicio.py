# Sugerido pelo Professor

import requests

# Numero 1:
"""
Implementa, em Python, um programa que faça o seguinte:
    Dada uma lista com 20 elementos, imprima no ecrã os elementos 12 a 16
"""

lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

def ex1():
    for i in range(11, 16, 1):
        print(i)


# Numero 2:
"""
Dado uma lista, elabora um programa que permita com um ciclo, inserir elementos na lista até que a tecla "q" seja precionada
"""

def ex2():
    while True:
            a = input("O que deseja comprar? ("q" para sair) ")
            if a.lower() == "q":
                print("Esta é a tua lista: ")
                for i in lista:
                    b = ", ".join(lista)
                print(b)
                break
            elif a:
                if a.lower() in lista:
                    print(f"{a} já está na lista")
                else:
                    lista.append(a.lower())

# Numero 3:
"""
Função que imprime a sequencia de Fibonacci até a um input
"""

def ex3():
    
    numero = int(input("Qual o digito para começar? "))
    if numero <= 1:
        print("Este número não se insere na função")
        numero = print("Insira outro: ")
    
    numero2 = int(input("Qual o digito para acabar? "))
    if numero2 <= 1:
        print("Este número não se insere na função")
        numero2 = print("Insira outro: ")
    

    a, b = 0, 1  # F1 = a = 0, F2 = b = 1

    for x in range(numero - 1):
        a, b = b, a + b

    for i in range(numero, numero2 + 1):
        print(f"F({i}) = {a}")
        a, b = b, a + b


# Numero 4:
def ex4():
    lista = ["maçã", "banana", "laranja"]

    for fruta in lista:
        if fruta == "banana":
            break

# Numero 5:
"""
Fazer uma função lamda para o cubo de um numero
"""
def ex5():
    lFunc = lambda a : a*a*a
    print("Escolha um número: ")
    a = input()
    lFunc(a)

def ex6():
    lFuncEx6 = lambda : [print(i) for i in range(11)]
    lFuncEx6()

def ex7():
    myDict = {
        "Key1": "Val1",
        "Key2": "Val2",
        "Key3": "Val3"}
    
    for key in myDict:
        print(f"{key}:", myDict[key])

# Exercicio 8
"""
App que consulta uma API pública e mostra os dados
"""

def ex8():
    print("=== Consulta de Pokémon ===")
    nome = input("Digite o nome de um Pokémon: ").lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # lança um erro de status no caso de erro

        dados = resposta.json() # pega a resposta, converte para json e aplica o json em um dicionario

        print(f"\nNome: {dados["name"].title()}")
        print(f"Pokedex: {dados["id"]}")
        print("Tipos:")
        for tipo in dados["types"]: # pokemons podem ter dois tipos, por isso um ciclo for
            print(f" - {tipo["type"]["name"].title()}")

        print("Habilidades:")
        for habilidade in dados["abilities"]: # pokemons podem ter varias habilidades tambem
            print(f" - {habilidade["ability"]["name"].replace("-", " ").title()}")

        print("\nStats:")
        for stats in dados["stats"]: # o ciclo for percorre o "stats", que é dividido entre vários "stat", pegando o nome (hp, defense, etc) e o seu valor (base_stat)
            print(f"{stats["stat"]["name"].replace("-", " ").title()}: {stats["base_stat"]}")
        total_base_stat = 0
        for bst in dados["stats"]: # o ciclo percorre o "stats" incrementando o valor de cada "stat" a total_base_set
            total_base_stat += bst["base_stat"]
        print(f"Base Stat Total: {total_base_stat}")

        print(f"\nAltura: {dados["height"] / 10:.1f} m") # divisao por 10 para a conversão a metros e quilos
        print(f"Peso: {dados["weight"] / 10:.1f} kg")

    except requests.exceptions.HTTPError: # no caso do HTTP nao existir
        print("Pokémon não encontrado. Verifique o nome digitado.")
    except requests.exceptions.RequestException as e: # no caso da API não poder ser acessada
        print(f"Erro ao acessar a API: {e}")

def main():
    ex8()
            
if __name__ == "__main__":
    main()