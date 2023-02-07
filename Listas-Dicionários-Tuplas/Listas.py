# Listas são um tipo de variável que permite o armazenamento de vários valores 

# Pode ser acessada pelo índice 

# Uma lista pode conter zero ou mais elementos inclisive conter outras listas 

# ------- O TAMANHO DE UMA LISTA É DETERMINADO PELO NÚMERO DE ELEMENTOS QUE ELA CONTEM ------ #


Lista = []

z = [15,8,9]

print(z[0]) # Mostrando na tela o elemento de índice 0

# Podemos mudar o conteúdo de um elemento

z[0] = 7

print(z)

# Calculo da média

notas =[6,7,5,8,9] # lista de notas que são atibuidas
soma = 0 
x = 0

while x<5: # lista de repetição de todas as notas  *** Lembrando que o indice vai de 0 a 4, por isso o x=0 ***
    soma += notas[x] # soma para pegar todas as notas 
    x += 1 # somando x para chegar até 4
print(f"Média: {soma / x:5.2f}") # Assim usamos a soma para dividir pela quantidade de elementos, sendo reaproveitado o x



# Fazendo uma modificação para a pessoa escrever as notas

notas2 = [0,0,0,0,0,0,0]
soma2 = 0
x2 = 0 
while x2<7:
    notas2[x2] = float(input("Digite a nota {x2}:")) # Repetição para pegar as notas 
    soma2 += notas2[x2] # fazendo a soma
    x2 += 1
x2 = 0   # reiniciando para criar uma nova repetição
while x2<7:  # repetição para imprimir a lista de notas completa 
    print(f"Nota {x2}: {notas2[x2]:6.2f}")
    x2 += 1
print(f"Média: {soma2 / x2:5.2f}") # Resultado final indentado



# Trabalhando com os índices


numeros = [0,0,0,0,0] 
   #índice 0,1,2,3,4
y = 0
while y<5:
    numeros[y] = int(input(f"Número {y + 1}:")) # adicionamos +1 ao y para não começar do índice 0
    y += 1
while True:
    escolhido = int(input("Que posição você quer imprimir? (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[escolhido - 1]}") # Operação inversa para obter o indice


# Cópia e Fatiamento de Listas

L = [1,2,3,4,5]

V = L    # Quando atribuimos um objeto a outro estamos apenas copiando a mesma referência, e não seus dados 

V[0] = 6  # Quando modificamos V também modificamos o L pois está atribuido na memória como algo igual

print(V)
print(L)

# Vejamos que quando modificamos V tambem modificamos L 
# Isto porque uma lista em Python é um objeto
# Nesse caso V e L são a mesma lista!!


# Para criarmos uma cópia ultilizamos:

L = [1,2,3,4,5]

V = L[:] # Ao escrevermos isso estamos referindo uma nova cópia de L

V[0] = 6 # Assim podemos alterá-las de maneira individual


# Fateamento

# Pode ser feito da mesma forma que uma String:

L = [1,2,3,4,5]

L[0:5]
# [1,2,3,4,5]

L[:5]
# [1,2,3,4,5]
L[:-1]
# [1,2,3,4]
L[1:3]
# [2,3]
L[1:4]
# [2,3,4]
L[3:]
# [4,5]


# Tamanho de Listas

# Podemos usar a função len com listas, o valor retornado é igual ao tamanho dela

L = [12,9,5]
print(len(L))
# 3

V = []
len(V)
# 0

# A função len() pode ser usada para o contorle do limite dos índices

L = [1,2,3]
x = 0
while x < 3:
    print(L[x])
    x += 1

# Isso pode ser reescrito como:

L = [1,2,3]
x = 0
while x < len(L):
    print(L[x])
    x += 1
# 1
# 2
# 3

# A vantagem desse ajuste se dá pelo aumento da lista, ou seja se aumentar mesmo assim vai continuar funcionando


# Adicionando Elementos a Lista

# Ultilzaremos .append após um objeto, ou seja, a própria lista 

# Assim teremos o método L.append(valor)

L = []

L.append("a")

# ['a']

L.append("b")

# ['a','b']

L.append("c")

# ['a','b','c']

len(L)

# 3

# Programa que adiciona elementos e imprime todos os adicionados

L = []
while True:
    n = int(input("Digite um número ( 0 para sair): "))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1

# Outra maneira de adicionar elementos a lista é usar +:

L = []
L = L + [1]
# [1]

L += [2]
# [1,2]

L += [3,4,5]
# [1,2,3,4,5]


# EXTEND

L = ["a"]
L.append("b")

L.extend(["c"])
# ["a","b","c"]

L.append(["d","e"])

# ['a','b',c,['d','e']]

L.extend["f","g","h"]

#['a','b',c,['d','e'],'f','g','h']

# Extend é usado para extender uma lista 

# O append vai adicionar uma lista inteira dentro da lista

L = ["a"]
L.append(["b"])
L.append(["c","d"])
len(L)
# 3
L[1]
# b
len(L[2])
# 2
L[2][1]
# 'd'

# Remoção de elementos da lista 

# Usando a intrução del

L = ["a","b","c"]
del L[1]
# ['a','c']

# Podemos apagar fatias inteiras com range

L = list(range(101))
del L[1:99]
# [0,99,100]

# list é ultilizado para transformar o resultado da função em lista 

