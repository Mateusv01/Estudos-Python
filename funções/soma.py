# Programa 8.19 - Módulo soma (soma.py) que importa a entrada (Módulos.py)
from Módulos import valida_inteiro

L = []
for x in range(10):
    L.append(valida_inteiro("Digite um número:", 0, 20))
print(f"Soma: {sum(L)}")

""" É muito útil informar o nome do módulo antes da função, porém podem ocorrer conflitos de nomes
    então é melhor usar a preposição import Módulos e Módulos.valida_inteiro"""