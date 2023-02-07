""" A função type retorna o tipo de variável função ou objeto"""

a = 5
print(type(a))

b = "Olá"
print(type(b))

c = False
print(type(c))

d = print
print(type(d))

""" O tipo retornado é uma classe, vejamos como usar isso em um programa
    Para verificar se o tipo de uma variável equivale a outro tipo, usaremos
    a função isinstance"""


import types

def diz_o_tipo(a):
    if isinstance(a, str):
        return "String"
    elif isinstance(a, list):
        return "Lista"
    elif isinstance(a, dict):
        return "Dicionário"  
    elif isinstance(a, int):
        return "Inteiro"
    elif isinstance(a, float):
        return "Decimal"
    elif isinstance(a, types.FunctionType):
        return "Função"
    elif isinstance(a, types.BuiltinMethodType):
        return "Função interna"
    else:
        return str(type(a))

print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo(None))


L = ["Alô", 2, ["!"], {"a": 1, "b": 2}]
for e in L:
    print(type(e))


# Programa 8.21 - Navegando listas a partir do tipo dos seus elementos

L = ["a", ["b", "c", "d"], "e"]
for x in L:
    if type(x) is str:
        print(x)
    else:
        print("Lista:", end="")
        for z in x:
            print(f"{z}", end="")
        print()


# Função recursiva que imprime os elementos da lista

ESPAÇOS_POR_NÍVEL = 4

def imprime_elementos(l,nivel=0):
    espacos = ' ' * ESPAÇOS_POR_NÍVEL * nivel
    if type(l)==list:
        print(espacos, "[")
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)

L=[1, [2,3,4,[5,6,7]]]

imprime_elementos(L)