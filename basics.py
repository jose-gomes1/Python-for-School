#Declaração de variáveis

idade = 17
nome = "José"
altura = 1,70
estudante = True

#Operadores aritméticos

print(idade + 1)
print(idade - 1)
print(idade / 2)
print(idade * 2)

#Operadores de comparação
print(idade > 18)
print(idade == 18)
print(idade != 18)
print(idade <= 18)
print(idade >= 18)
print(idade >= 18 and estudante)
print(idade >= 18 or estudante)
print(not estudante)

#Instruções condicionais

idade = int(input("Qual a tua idade? "))

if idade < 18:
    print("Menor de idade")
elif idade > 18:
    print("Maior de idade")
else:
    print("Acabaste de fazer 18")