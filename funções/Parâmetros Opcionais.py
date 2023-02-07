""" Parâmetros opcionais são úteis para evitar a passagem desnecessária dos mesmos vaores
    """

""" Nem sempre precisamos passar parâmetros para as funções como:"""

# Função que imprime uma linha na tela 

def barra():
    print("*" * 40)

barra()

""" Porém podemos usar parâmetros opcionais para especificar nossa função"""

def barra_opcional(n=40, caractere="*"):
    print(caractere * n)

barra_opcional()

""" Podemos combinar os parâmetros opcionais com obrigatórios na mesma função"""

def soma(a,b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s
print(soma(3, 4, True))

""" Embora possamos combinar parâmetros opcionais com obrigatórios, eles não podem ser misturados
    os Parâmetros opcionais sempre devem ser os últimos"""

# -------------------------------------|
#          Nomeando Parâmetros         |
# -------------------------------------|

""" Python suporta a chamada de funções com vários parâmetros. Quando especificamos o nome de um parâmetro
    Podemos passa-los em qualquer ordem"""


def retangulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)

retangulo(10,10)


# -------------------------------------|
#       Funções como Parâmetro         |
# -------------------------------------|


""" Exemplo de funções que realizam uma única tarefa"""

# Programa 8.12 - funcões como parâmetro
def soma1(a,b):
    return a + b

def subtração(a, b):
    return a - b
def imprime(a, b, foper):
    print(foper(a,b))
imprime(5, 4, soma)
imprime(10, 1, subtração)



# Programa 8.13 - Configuração de funções com funções

def imprime_lista(L, fimpressão, fcondição):
    for e in L:
        if fcondição(e):
            fimpressão(e)
def imprime_elemento(e):
    print(f"Valor: {e}")
def épar(x):
    return x % 2 == 0
def éimpar(x):
    return not épar(x)

L = [1, 7, 9, 2, 11, 0]

imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)

# ----------------------------------------------|
# Empacotamento e desempacotamento de parâmetros|
# ----------------------------------------------|


""" Outra flexibilidade da linguagem Python é passar parâmetros empacotados em uma lista"""

def soma2(a,b):
    print(a + b)
P = [2, 3]

soma2(*P)

""" Exemplo em que usamos uma lista de listas para realizar várias chamadas de uma função"""

def barra2(n=10, c="*"):
    print(c * n)
G = [[5, "-"], [10, "*"], [6, "."]]

for e in G:
    barra2(*e)


# ----------------------------------------------|
#     Desempacotamento de parâmetros            |
# ----------------------------------------------|


""" Podemos criar funções que recebem um número indeterminado de parâmetros ultilizando listas de parâmetros"""

# Programa 8.14 - Função soma com número indeterminado de parâmetros

def soma3(*args):
    s = 0
    for x in args:
        s += x
    return s

print(soma3(1, 2))

""" Também podemos criar funções que combinem parâmetros obrigatórios e uma lista de parâmetros"""

# Programa 8.15 - Função imprime maior numero com número indeterminado de parametros 

def imprime_maior_número(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
        print(mensagem, maior)

imprime_maior_número("Maior", 5, 4, 3, 1)
imprime_maior_número("Max:", *[1, 7, 9]) 

# ----------------------------------|
#          Função Lambda            |
# ----------------------------------|

""" Podemos criar funções sem nome, chamadas de função labmda"""

# Programa 8.16 - Função lambda que recebe um valor e retorna o dobro dele

a = lambda x: x * 2
print(a(3))

# Programa 8.17 - Função lambda que recebe mais de um parâmetro

aumento = lambda a, b: (a * b/ 100)
print(aumento(100, 5))

F = ["A", "b", "C", "d", "E"]

F.sort()
print(F)

F.sort(key=lambda k: k.lower())

print(F)


