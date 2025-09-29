# listas -> arrays []
# dictionary -> par chave -> valor {like:json}
# sets -> mutáveis {}
# tuplet -> imutáveis ()

# funções lambda
# funções anónimas de baixa complexidade

# exercício 1 (5m)
"""
Programa onde é definido um tuplet com 4 valores e uma função que aceita como parâmetro um tuplet e que imprime no ecrã o seu conteúdo
"""

meuTuplet = ("val1", "val2", "val3", "val4")

def funcTuplet(tuplet):
    for i in tuplet:
        b = ", ".join(tuplet)
    print(b)
    
funcTuplet(meuTuplet)