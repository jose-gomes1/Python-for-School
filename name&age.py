from datetime import date

name = input("Como te chamas?\n")
ano = input("Qual o teu ano de nascimento?\n")
hoje = date.today()
idade = hoje.year - int(ano)

respostas_true = ["sim","true","correto","verdade","1"]
respostas_false = ["não","nao","incorreto","falso", "false","0"]

print(f"O teu nome é", name, "e tens", idade, "anos")
booleano = input("És maior de idade?\n").lower()
if booleano in respostas_true:
    if idade >= 18:
        print("És maior de idade")
    else:
        print("Estás a mentir")
elif booleano in respostas_false:
    if idade < 18:
        print("És menor de idade")
    else:
        print("Estás a mentir")
else:
    print("Resposta inválida")