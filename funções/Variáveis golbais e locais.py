""" A variável global fica definida fora de uma função, podendo ser usada em qualquer uma, 
    Enquanto a variável local só existe dentro de uma função"""

# Exemplo dos dois casos

Empresa = "Unidos Venceremos ltda"

def imprime_cabeçalho():
    print(Empresa)
    print("-" * len(Empresa))

imprime_cabeçalho()


""" *IMPORTANTE* Usar as variáveis globais apenas em caso de valores constantes, como o nome da empresa
    é preciso tomar cuidado quando alterar uma variável global dentro da função"""

a = 5
def muda_e_imprime():
    a = 7
    print(f"a dentro da função: {a}")
print(f"a antes de mudar: {a}")
muda_e_imprime()
print(f"a Depois de mudar: {a}")

# Função não mudou a variável global

""" Se quisermos modificar uma variável global dentro de uma função, devemos informar que ela é uma variáel
    global com a instrução global"""

a = 5
def muda_e_imprime2():
    global a
    a = 7
    print(f"a dentro da função: {a}")
print(f"a antes de mudar: {a}")
muda_e_imprime2()
print(f"a Depois de mudar: {a}")

# Função modificou a variável global


# -------------------------------------|
#          Funções Recursivas          |
# -------------------------------------|

""" Uma função pode chamar a si mesma, quando isso ocorre ela é uma função recursiva """

# Função recursiva para calculo do fatorial

# def fatorial(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return n * fatorial(n - 1)

# Programa 8.6 - Para facilitar o rastreamento

def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"Fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f"Fatorial de {n} = {fat}")
    return fat

fatorial(4)


""" A sequência de fibonacci é um problema clássico que podemos aplicar na função recursiva 
    Começa com dois números 0 e 1 assim sendo somado o número seguinte com seu anterior
    0, 1, 1, 2, 3, 5, 8, 13, 21
    
    A Função recursiva fica definida como
    n <= 1 ; n ; fibonacci(n - 1) + fibonacci (n - 2); """

 # Função recursiva de fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)


# Função recursiva que calcula o MDC

def maior_divisor_comum(a, b):
    if b == 0:
        return a
    
    return maior_divisor_comum(b, a % b)


print(maior_divisor_comum(32,24))

# Função para calcular o MMC

def mmc(a,b):
    return abs(a * b) / maior_divisor_comum(a, b)

print(f"MMC 5 e 3 -->   {mmc(5, 3)}")

# -------------------------------------|
#             Validação                |
# -------------------------------------|

""" Funções são muito úteis para validar a entrada de dados"""

# Exemplo de validação sem usar uma função

while True:
    v = int(input("Digite um valor ente 0 e 5"))
    if v < 0 or v > 5:
        print("Valor inválido")
    else:
        break

""" Podemos transformá-lo em uma função que receba a pergunta de valores máximo e mínimo"""

# Validação de inteiro usando função
def faixa_int(pergunta, máximo, mínimo):
    while True:
        v = int(input(pergunta))
        if v < mínimo or v > máximo:
            print(f"Valor inválido. Digite um valor entre {mínimo} e {máximo}")
        else:
            return v

print(faixa_int("Digite um valor", 5, 1))


# Validação tamanho da string

def string_val(palavra, min_carac, max_carac):
    tamanho = len(palavra)
    return min_carac <= tamanho <= max_carac

print(string_val("amar", 1, 5))

def procura_string(s, lista):
    return s in lista

L = ["abacaxi", "ovo", "manteiga"]

print(procura_string("ovo", L))


def valida(validas):
    validas = validas.lower()
    while True:
        opção = input("Digite uma opção: ").lower()
        if opção in validas:
            return opção
        print(f"Opção inválida, tente novamente")

print(valida("abacaxi"))