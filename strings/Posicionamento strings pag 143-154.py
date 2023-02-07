# Métodos de apresentar as strings de formas mais interessantes 

# |-------------------------------------|
# |            Center                   |
# |-------------------------------------|


# O método center, centraliza a string em um número de posições passado como parâmetro, preenchendo espaços a 
# direita e a esquerda até que esteja centralizada

s = "Mateus"

print("|" + s.center(10) + "|")

print("|" + s.center(10, ".") + "|")


# Se deseja completar a string com espaços a esquerda, pode usar o método ljust, a direita rjust

print(s.ljust(20))
print(s.rjust(20))
print(s.ljust(20,"-"))
print(s.rjust(20,"."))

# Essas funções são úteis quando precisamos criar relatórios ou alinhar a saida do programa.


# |-------------------------------------|
# |         Split/Splitlines            |
# |-------------------------------------|

# QUEBRA OU SEPARÇÃO DE STRINGS 

# O método split quebra uma string a partir de um caractere passado como parâmetro

s = "Um passarinho, dois passarinhos, três passarinhos"
print(s.split(","))
print(s.split(" "))

# O caractere usado para dividir não é retornado na lista, ele é ultilizado e depois descartado

# Se deseja separar uma string com várias linhas de texto, pode usar o método splitlines()

f = "Primeira linha\nSegunda linha\nTerceira linha"
print(f.splitlines())


# |-------------------------------------|
# |      Substituição de Strings        |
# |-------------------------------------|

# Para subistituir treichos por outros, ultilize replace 

# O primeiro parâmetro é a string a subistituir, o segundo é o conteúdo que a substitúira 
# Opcionalmente podemos usar um terceiro parâmetro que limita quantas vezes podemos fazer a repetição
s = "um tigre, dois tigres, três tigres"
print(s.replace("tigres","gatos"))

print(s.replace("tigres","gatos",1))

print(s.replace("","."))

# Se não adicionar nada na primeira string, os espaços em branco serão oculpados pelo segundo parâmetro



# |-------------------------------------|
# |    REMOÇÃO DE ESPAÇOS EM BRANCO     |
# |-------------------------------------|

# O método strip é usado para remover espalos em branco do inicio ou fim da string
# Já os métodos lstrip e rstrip removem apenas os vcaracteres em branco a diireita e a esquerda respectivamente

t = "   Olá   "

print(t.strip())
print(t.lstrip())
print(t.rstrip())

# Podemos passar um parâmetro como caractere para remover

s = "...///Olá///..."

print(s.lstrip("."))
print(s.rstrip("."))
print(s.strip("."))
print(s.strip("./"))


# |-------------------------------------|
# |  VALIDAÇÃO DO TIPO DE CONTEÚDO      |
# |-------------------------------------|

# Strings podem ser verifcadas ultilizando-se métodos especiais. Esses métodos verificam se todos os caracteres
# são letras ou números ou uma cobinação deles

s = "123"
p = "alô mundo"

print(p.isalnum())
# FALSE
print(s.isalnum())
# TRUE
print(s.isalpha())
# FALSE

# O método .isanum() retorna um boolean verdadeiro quando a string só tem números
# Se a string tiver algum caractere como !,?,* (vai retornar Falso)

# O método .isalpha() é mais restritivo, retornando verdadeiro apenas se todos os caracteres forem letras
# retorna falso se algum outro tipo de caractere for encontrado ou se a string estiver vazia

# O método .isdigit() verifica se o valor consiste em números retornando True se a string não estiver vazia
# contendo apenas números

# OBS: Se a string contiver espaços, pontos, vírgulas ou sinais (+ ou -), retorna falso:

print("771".isdigit())
print("10.5".isdigit())


# OS MÉTODOS isdigit() e isnumeric() SÃO PARECIDOS, SUA DIFERENÇA ENVOLVE O CONHECIMENTO DO UNICODE 
# APROFUNDADO, O MÉTODO isdigit() retorna True para cada número Unicode 
# ENQUANTO o método isnumeric() é mais abrangente 
# EXEMPLO:

umterco = "\u2153"
novetibetano = "\u0f29"

print(umterco.isdigit())
print(novetibetano.isdigit())
print(novetibetano.isnumeric())
print(umterco.isnumeric())

# Podemos verificar se todos os caracteres são maiúsculas ou minúsculas 
# Usando islower() ou isupper()


# Temos como verificar se a string contém apenas caracteres em brancos, como espaços, marcas de tabulação(TAB)
# quebras de linha (LF) ou retorno de carro (CR) para isso vamos usar o método isspace()

print("\t\n\r".isspace())
print("\tAlô".isspace())



# Se quiser verificar se algo é printável na tela o método .isprintable()
# Ele da False quando temos caracteres que não vão ser printados na tela como \n

print("\n\t".isprintable())
print("\nAlô".isprintable())
print("Alô".isprintable())


# |-------------------------------------|
# |       FORMATAÇÃO DE STRINGS         |
# |-------------------------------------|

# Usando o format podemos substituir valores usando números entre chaves 
# Cada número representa a posição que o valor vai subistituir

print("{0} {1}".format("Alô","Mundo"))

print("{0} x {1} R${2}".format(5,"maçã","1.20"))

# O número entre chaves é uma referencia aos parâmetros passados como:

print("{0} {1} {0}".format("-","x"))

# Isso permite a completa reordenação da mensagem 

print("{1} {0}".format("primeiro","segundo"))
# primero = 0
# segundo = 1
# como uma lista 

# Essa sintaxe permite especificar a largura de cada valor usando o símbolo de (:) como 
# no parâmetro 0:10 no exemplo:

print("{0:10} {1}".format("123","154"))

# Que significa : subistitua o primeiro parâmetro com uma largura de 10 caracteres 

# Se o parâmetro for menor que o número informado o espaço vai preencher 

# MÉTODOS DO FORMAT

# (^) USADO PARA CENTRALIZAR OS VALORES ENTRE OS ESPAÇOS

print("X{0:^10}X".format("123"))
#X   123    X


# (<) PARA COLOCAR OUTRO CARACTERE NO LUGAR DE ESPAÇOS, PODEMOS ESPECIFICAR LOGO DEPOIS DE DOIS PONTOS :

print("X{0:!<10}X".format("123"))

# OU (>)

print("X{0:.>10}".format("123"))

# USANDO DENTRO DE UMA LISTA COM O ÍNDICE 

print("{0[0]} {0[1]}".format(["123","456"]))

# VÁLIDO PARA OS DICIONÁRIOS

# OBS: O MÉTODO format COMPETE DIRETAMENTE COM AS fstrings DEPENDENDO DE CADA PROGRAMA
# QUANDO O PROGRAMA É MAIS COMPLEXO O format PODE SER MAIS INTERESSANTE


# FORMATAÇÃO DE NÚMEROS

# podemos formatar números especificando o tamanho a imprimir com um zero a esquerda

print("{0:05}".format(5))
#00005
print()
print()
# As funções vistas antes como (^),(<) e (>) podem ser usados 

# PODEMOS USAR UMA VÍRGULA PARA SOLICITAR O AGRUPAMENTO POR MILHAR, E O PONTO PARA INDICAR A QUANTIDADE DE 
# NÚMEROS APÓS A VÍRGULA

print("{0:10,}".format(7243))
print("{0:10,.5f}".format(1500.31))
print("{0:10.5f}".format(1500.31))



# Outro caso é quando trabalhamos com formatos numéricos, devemos indicar com uma letra o formato que deve 
# ser inserido, essa letra informa como o número será lido

# TABELA DE CÓDIGOS

#        CÓDIGO       |   DESCRIÇÃO  |                  EXEMPLO (45)
#          b               Binário                         101101
#          c               Caractere                         - 
#          d               Base 10                           45
#          n               Base 10 local                     45
#          o               Octal                             55
#          x            Hexadecimal com letras minusculas    2d
#          X            Hexadecimal com letras maiúscuas     2D




# FORMATO DE NÚMEROS DECIMAIS 

#        CÓDIGO                    |   DESCRIÇÃO  |                                 EXEMPLO (1.345)
#          e               Notação científica com e minúsculo                       1.345000e+00
#          E               Notação científica com E maiúsculo                       1.345000E+00
#          d               Decimal                                                   1.345000
#          g               Genérico                                                  1.345
#          G               Genérico                                                  1.345
#          n               Local                                                    1,345
#          %               Percentual                                              134.500000%





# EXEMPLOS:

print("{:b}".format(5678))

# O b imprime usando o sistema binário com 0 e 1 de dígitos 

print("{:c}".format(65))

# O c imprime o número transformando em caractere segundo a tabela Unicode 

print("{:o}".format(5678))

# O o imprime o número usando o sistema octal ou seja, de base 8

print("{:x}".format(5678))

# O x e X imprimem usando o sistema hexadecima, base 16 a diferença é o tamanho das letras 

# O d e n são parecidos 
# A única diferença é que n leva as configurações regionais da máquina 

# Antes de configurar para ptbr, os resultados eram iguais

print("{:d}".format(5678))
print("{:n}".format(5678))

# Configurando em ptbr
import locale
locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")

print("{:n}".format(5678))


# -------------------------------------------------------------------------------------

# Para números decimais, temos vários códigos. O código "{:f}", que quando configurado separa os milhares em 
# vírgula e ponto

print("{:f}".format(1567.543))
import locale
locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")

print("{:n}".format(1567.543))


# ------------------------------------------------------------------------

# NOTAÇÃO CIENTÍFICA

# Os formatos e/E imprimem o número usando notação científica 

# Por exemplo: 1004.5 em notação seria expresso como 1.004500e+03

# Lembrando que a notação sempre é na base 10

# Agora refazendo a prova da conta 1.0004500e+03 ou seja:

# 1.004500e+03 x 10^3 = 1.004500 x 1000 = 1004.5

# $$ O formato g/G são chamados de genéricos, pois dependendo do número são exibidos no formato f ou e

# Exemplos:

print("{:8g}".format(3.1415926589))
print("{:8G}".format(3.1415926589))

print("{:8g}".format(3.14))
print("{:8G}".format(3.14))

print("{:5.2%}".format(0.05))