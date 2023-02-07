""" Para definir uma nova função ultilizaremos a instrução def """

# Função de soma

def soma(a,b):
    print(a + b)

soma(1,2)
soma(3,4)

""" Funções são especialmente interessantes para isolar uma tarefa específica
    em um trecho de programa. Permitindo a solução do problema seja reutilizada
    em outras partes do programa"""

# Função de soma retornando a,b

def soma_return(a,b):
    return (a + b)
soma_return(2,9)

""" Quando ultilizamos return para indicar um valor a retornar. Observe que o print
    não é mais usado na função, sendo muito interessante para separar o cálculo da
    impressão """

# Função retorna verdadeiro ou falso 

def épar(x):
    return x % 2 == 0
print(épar(2))
print(épar(3))
print(épar(10))

""" Agora precisamos definir uma função para retornar a palavra par ou ímpar"""

def par_ou_ímpar(x):
    if épar(x):
        return "par"
    else:
        return "ímpar"
    
print(par_ou_ímpar(4))
print(par_ou_ímpar(5))


""" EXERCICIOS """

# Função que retorne o mair entre dois números

def maior_num(a,b):
    if a > b:
        return a
    else:
        return b 

print(maior_num(1,2))
print(maior_num(90,40))

# Função que retorne True se o primeiro for múltiplo do segundo

def múltiplo(a,b):
    return a % b  == 0

print(múltiplo(8,4))
print(múltiplo(7,3))
print(múltiplo(5,5))

# Funçã que receba o lado e calcule a área
 
def área_quadrado(x):
    return x ** 2

print(área_quadrado(4))
print(área_quadrado(9))

# Função que receba a base e a altura de um triângulo e retorne sua área

def área_triângulo(b,h):
    return (b * h) / 2

print(área_triângulo(6,9))
print(área_triângulo(5,8)) 



""" Exemplo de função de pesquisa """

# Pesquisa em uma lista 

def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None


L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))


# Calculando a média dos valores de uma lista

def somar(L):
    total = 0
    for e in L:
        total += e
    return total / len(L)

print(somar(L))


""" Devemos sempre atentar para deixar o código mais simples e usual possível
    sempre atentando a não limita-lo"""

# Calculo do fatorial

def fatorial(n):
    fat = 1 
    while n > 1:
        fat *= n
        n -= 1
    return fat

print(fatorial(4))


# Reescrevendo programa 8.2

def soma2(L):
    total = 0
    for e in L:
        total += e
    return total

L = [1, 7, 2, 9, 15]
print(soma2(L))



""" DICA : PYTHON tem funções para calcular o máximo/ soma / mínimo de uma lista"""


P = [4, 5, 8, 44, 10]

print(sum(P))
print(max(P))
print(min(P))