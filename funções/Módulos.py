""" Depois de criar várias funções, os programas ficam muito grandes e de alguma forma 
    precisamos usá-las o Python resolve o problema com o comando import"""


# Programa 8.18 - Módulo de entrada (entrada.py)

def valida_inteiro(mensagem, mínimo, máximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= mínimo and v <= máximo:
                return v
            else:
                print(f"Digite um valor entre {mínimo} e {máximo}")
        except ValueError:
            print("Você deve apenas digitar um número inteiro")


""" O programa acima foi importado no arquivo soma.py, sendo assim usado mesmo estando em outro arquivo"""

# -------------------------------------|
#          Números Aleatórios          |
# -------------------------------------|


import random

""" Para gerar números aleatórios é preciso usar o módulo random que traz várias funções
    para gerar números randômicos"""


for x in range(10):
    print(random.randint(1,100))

""" Ou seja, a função fez a impressão de 10 números aleatórios entre 1 e 100, que não se repetem"""


# Programa 8.20 - Advinhando o número

n = random.randint(1, 10)
tentativas = 0
while tentativas < 3:
    x = int(input("Escolha um número entre 1 a 10: "))
    if x == n: 
        print("Você acertou!!!!")
        break
    else: 
        print(f"Você errou")
        tentativas += 1


""" Podemos gerar números aleatórios fracionários ou de ponto flutuante com random"""

for x in range(10):
    print(random.random())

""" Para obter valores fracionários dentro de uma determinada faixa, usamos a função uniform"""

for x in range(10):
    print(random.uniform(15, 25))

""" Podemos usar a função sample para escolher alatoriament elementos de uma lista
    Essa função recebe a lista e quantidade de amostras ou elementos que queremos retornar"""

print(random.sample(range(1, 101), 6))

""" Se quisermos embaralhar uma lista podemos usar a função shuffle"""


a = list(range(1, 11))
random.shuffle(a)
print(a)