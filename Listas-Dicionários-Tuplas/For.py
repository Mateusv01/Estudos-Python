# Python apresenta uma repetição especialmente projetada para percorrer lista
# A instrução For funciona de forma parecida com While
# Mas a cada repetição ultiliza um elemento diferente da lista 



L = [8,9,15]
for e in L:
     print(e)

# Quando começamos a executar for em "for e in L: " temos e = ao primeiro elemento da lista
# Em "print(e) imprimimos 8 e a execução volta no for, fazendo agora o elemento valer 9, assim por diante"

# Para fazermos a mesma coisa com While:

LI = [8,9,15]
x = 0
while x < 3:
    f = LI[x]
    print(f)
    x += 1

# Embora for facilite nosso tabalho, ela não subistitui completamente o while
# Dependendo do problema, usaremos For ou While

# Normalmente usamos for quando quisemos processar os elementos de uma lista, um a um
# while é indicado para repetições nas quais não sabemos quantas vezes vamos repetir ou onde manipulamos os índices de forma não sequencial


# USO DO BREAK COM FOR

LIS = [7,8,9,10]
p = int(input("Digite um número a pesquisar: "))
for i in LIS:
     if i == p:
          print("Elemento encontrado")
          break
else:
 print("Elemento não encontrado!")


 # Reescrevendo o Programa 6.6 com for
  # adicionando elementos a lista

lista = []
while True:
     pergunta = int(input("Digite um número (0 sai): "))
     if pergunta == 0:
          break
     lista.append(pergunta)
for l in lista:
     print(l)

# Não podemos substituir o while, por que desconhecemos o número de elementos na lista
# já que eles são adicionados



# -------------------------------------|
#              RANGE                   |
# -------------------------------------|


# Podemos ultilizar as funções Range para gerar listas simples
# A função range não retorna uma lista propriamente dita, é mais um generator

# Imagine um programa que imprima 0 a 9 na tela

for v in range(10):
     print(v)

# Ele normalmente gera valores a partir de 0, então quando iformamos 10, falamos onde parar

# A vantagem de usar range é gerar listas eficientemente e com parâmetros

for o in range(5,8):
     print(o)

# Usando como incio o 5 e 8 como final

# Podemos acrescentar um terceiro parâmetro

range(0,10,2)

# Estamos gerando os pares entre 0 e 10, somando 2

#-------------------------------------------------------#
for t in range(3,33,3):
     print(t, end=" ")
print()

#------------------------------------------------------#

# Neste exemplo usamos uma construção especial com print()
# t é o valor que queremos imprimir
# com end=" " indicamos uma função para pular a linha 
# vejamos que o gerador retornado por range não é uma lista
# mesmo funcionando de forma parecida

# Para tranformar range numa lista é só usar a função list

# TRANSFORMANDO DE UMA RANGE EM UMA LISTA

listinha = list(range(100,1000,50))
print(listinha)


# -------------------------------------|
#            ENUMERATE                 |
# -------------------------------------|


# Com a função enumerate podemos ampliar as funcionalidades de for

# Vejamos como imprimir uma lista, em que temos um ídice entre colchetes na sua direita

W = [5,9,13]
g = 0
for y in W:
     print(f"[{g}] {y}")
     g += 1

# O mesmo programa usando a função enumerate:

lista_numeros = [5,9,13]
for i in enumerate(lista_numeros):
     r, z = i
     print(f"[{r}] {z}")
     print(i)

# A função enumerate gera uma tupla em que o primeiro valor é o índice e o segundo é o elemento
# da lista sendo enumerada 
# Ao usar r, z em for indicamos que o valor da tupla deve ser colocado no r e o segundo no z
# Ou seja, teremos (O,5) em que r = 0 z = 5
# O gerador enumerate retorna cada vez mais uma tupla, (1,9) e (2,13)