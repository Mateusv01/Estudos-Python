""" Em Python para abrir um arquivo ultilizamos open



    TABELA- MODOS DE ABETURA DE ARQUIVO 
    
    r        =       leitura                  
    w        =       Escrita, apaga o conteúdo se já existir
    a        =       Escrita, mas preserva os conteúdos que já existem
    b        =       Binário
    +        =       Atualização(leitura e escrita)             
    
    
    Os modos podem ser combinados ("r+","w+","r+b") """



""" A função open retorna um objeto do tipo file(arquivo) 
    Ao trabalhar com arquivo ultilizamos o seguinte ciclo: abertura, leitura e/ou escrita, fechamento
    Usamos write para escrever;
    read para ler;
    e close para fechá-lo;
    """

''' Vejamos um exemplo em que vamos escrever o arquivo números.txt com 100 linhas com números'''

arquivo = open("números.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

''' Uso do with, que permite criarmos contexto, ou seja, um bloco em que um objeto é válido'''

with open("números.txt","r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
        

''' Uso do with não precisa de fechamento e protege o arquivo de exceções'''


# -------------------------------------|
#    Parâmetros de linha de comando    |
# -------------------------------------|


""" Podemos acessar parâmetros passados ao programa na linha de comando ultilizando o módulo sys 
    Trabalhando com a linha argv"""


import sys
print(f"Números de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")



# Verifica se os parâmetros foram passados
if len(sys.argv) != 4:  # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-02.py nome_do_arquivo inicio fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open("números.txt", "r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])
    arquivo.close()




# -------------------------------------|
#       Geração de arquivos            |
# -------------------------------------|

""" Vejamos o programa que gera dois arquivos com 500 linhas cada. O programa distribui
    os números ímpares e pares em arquivos diferentes"""

# Programa 9.3 - Gravação de números pares e ímpares em arquivos diferentes

with open("ímpares.txt", "w") as ímpares:
    with open("pares.txt", "w") as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                ímpares.write(f"{n}\n")




# -------------------------------------|
#          Leitura e escrita           |
# -------------------------------------|


""" Podemos realizar diversas operações com arquivos como ler, processar e gerar novos
    Usando o programa anterior, vamos filtrá-lo para gerar um novo arquivo com números
    múltiplos de 4"""

with open ("múltiplos de 4.txt", "w") as múltiplos4:
    with open("pares.txt") as pares:
        for l in pares.readlines():
            if int(l) % 4 == 0:
                múltiplos4.write(l)

    


def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        # Verifica se conseguiu ler algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip() != "":
            return int(número)


def escreve_número(arquivo, n):
    arquivo.write(f"{n}\n")


pares = open("pares.txt", "r")
ímpares = open("ímpares.txt", "r")
pares_ímpares = open("pareseimpares.txt", "w")
npar = lê_número(pares)
nímpar = lê_número(ímpares)
while True:
    if npar is None and nímpar is None:  # Termina se ambos forem None
        break
    if npar is not None and (nímpar is None or npar <= nímpar):
        escreve_número(pares_ímpares, npar)
        npar = lê_número(pares)
    if nímpar is not None and (npar is None or nímpar <= npar):
        escreve_número(pares_ímpares, nímpar)
        nímpar = lê_número(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()



# 9.5 

pares = open("pares.txt", "r")
invertido = open("paresinvertidos.txt", "w")

inversão = pares.readlines()
inversão.reverse()
for l in inversão:
    invertido.write(l)  

pares.close()
invertido.close()