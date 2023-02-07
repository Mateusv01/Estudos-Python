# São uma estrutura de dados que implementam operações de união, intersecção e diferença
# a sua principal caracteristica é não admitir repetição como conjuntos
# Vejamos algumas operações com conjuntos



a = set()
a.add(1)
a.add(2)
a.add(3)
print(a)

a.add(1)
print(a)

# No exemplo adicionamos 1 pela segunda vez, e nada alteramos o conjunto em si, já que 1 
# já fazia parte 

a.add(0)
a.add(-1)
print(a)

# Podemos testar se um elemento faz parte de um conjunto ultilizando o operador in

print(1 in a)
print(-2 in a)

# Um set(conjunto) pode ser criado a partir de listas, tuplas e qualque outra estrutura
# que seja enumerável

b = set([2,3])
print(b)

# Entre as operações disponíveis temos a diferença entre conjuntos que usa - :

a = {0,1,2,3,-1}
b = {2,3}
print(a-b)

# {0, 1, -1} o resultado contém os elementos de a que não estão presentes em b

# A união é realizada pelo operador |:

a = {0,1,2,3,-1}
b = {2,3}
c = set([4,5,6])

print(a|b)
print(a|c)

# Conjunto set também possui outras propriedades, como tamanho (len)


# Exercício 6.19-

lista1 = set([2,4,6,8])
lista2 = set([2,3,5,8])

valores_comuns = lista1 & lista2
elementos_nao_repetidos = lista1 - lista2
primeira_sem_repetidos = lista1 - lista2

print(f"Primeira lista: {lista1}")
print(f"Segunda lista: {lista2}\n")


print(f"Os valores comuns da lista são: {valores_comuns}")
print(f"Não repetidos: {elementos_nao_repetidos}")
print(f"A primeira lista sem os repetidos da segunda: {primeira_sem_repetidos}\n")



# Exercício 6.20 - 

lista_velha = [1,3,5,7,9,11]
lista_nova = [1,2,3,4,5,6,7,8,9,10,]

conjunto1 = set(lista_velha)
conjunto2 = set(lista_nova)

não_mudou = conjunto1 & conjunto2

print(f"Os elementos que não mudaram: {não_mudou}")

novos_elementos = conjunto2 - conjunto1

print(f"Novos elementos: {novos_elementos}")

elementos_removidos = conjunto1 - conjunto2

print(f"Elementos que foram removidos: {elementos_removidos}")


