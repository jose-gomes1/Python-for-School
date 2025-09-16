from datetime import date

name = input("Como te chamas?\n")
ano = input("Qual o teu ano de nascimento?\n")
hoje = date.today()

print(f"O teu nome é", name, "e tens", hoje.year - int(ano), "anos")