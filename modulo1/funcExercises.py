# Exercício 1
"""
Vamos voltar às funções
Faz uma função que receba um set e dentro da função, um a um, os elementos do set são transferidos para outro set
"""

setA = set({1, 2, 3, 4, 5})

def funcSets(oMeuSet):
    setB = set()
    for i in oMeuSet.copy():
        valSet = oMeuSet.pop()
        setB.add(valSet)

    print("Set A:",setA)
    print("Set B:",setB)

# funcSets()

# Exercício 2
"""

"""