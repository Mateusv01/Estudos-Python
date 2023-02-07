# -------------------------------------|
#              TUPLAS                  |
# -------------------------------------|



# Tuplas são como listas imutáveis

# São ideias para representar uma lista com valores constantes e para realizar
# operações de empacotamento e desempacotamento de valores

# Tuplas são criadas de forma semelhantes a listas mas ultilizamos parênteses
# em vez de colchetes:

tupla = ("a","b","c")
print(tupla)

#----------------------------------------------------

# OBS: tuplas podem ser criadas sem os parênteses()

# tupla = "a","b","c"

#----------------------------------------------------

# Tuplas suportam a maior parte das operações com listas 

print(tupla[0])
print(tupla[1])

print(tupla[:1])
print(tupla * 2)

print(len(tupla))

# OBS: Mas as tuplas não podem ter seus elementos alterados 
# Dando erro caso tente modificar


# Podemos usar varias funções para gerar tuplas

for elemento in tupla:
    print(elemento)



# Outro exemplo com tuplas

tupla2 = 100,200,300
print(tupla2)

# (100,200,300) ---> empacotamento, ou seja, os números foram transformados em uma tupla

# -----------------------

a, b = 10, 20

print(a)
print(b)

# Desempacotamento --> esse tipo de construção permite distribuir o valor da tupla em várias variáveis
#                      também podemos trocar rapidamente o valor das variáveis

a, b = b, a
print(a)
print(b)



#  /                      /
# /    Uso da vírgula    /
#/                      /

# É muito importante o uso da virgula para não demostrar um número inteiro!



# Podemos criar tuplas a partir de listas com a função tuple()

L = [1,2,3]
T = tuple(L)
print(T)

# Apesar de não poder modificar os elementos podemos concatena-las e gerar novas tuplas


# Observe que se uma tupla contiver uma lista ou outro objeto que pode ser alterado, ela continuará funcionando
# normalmente, tupla que contém uma lista:

tupla3 = ("a",["b","c","d"])
print(tupla3)
print(len(tupla3))
print(tupla3[1])

tupla3[1].append("e")

print(tupla3)


#  /                                                     /
# /    Operações de empacotamento e desempacotamento    /
#/                                                     /

#  As operações funcionam com listas

c,d = 1, 2
print(c)
print(d)

c, e = [3,4]
print(c)
print(e)


# Podemos usar * para indicar vários valores a desempacotar

*a, b = [1,2,3,4,5]
print(a)
print(b)

a, *b = [1,2,3,4,5]
print(a)
print(b)

# No caso de *a = colocamos o último valor de b e outros em a
# No caso de *b = colocamos o primeiro valor de a e outros em b

# O uso do * indica o recebimento dos valores que sobraram após a divisão

a,*b, c = [1,2,3,4,5]
print(a)
print(b)
print(c)