# -------------------------------------|
#           ORDENAÇÃO                  |
# -------------------------------------|

# Até agora os itens da lista apresentam na mesma ordem que são digitados

# Método de ordenação com Bubble Sort (De Bolhas)

# Por ser lento não devemos usar em listas grandes


# A ordenação pelo método de bolhas consiste me comparar dois elementos a cada vez
# Se o valor do primeiro for maior que o segundo eles trocam de posição 
# O método de bolhas exige que a gente percorra a lista várias vezes 
# Esse método tem outra propriedade que é posicionar o maior elemento no final da lista

# Ordenação com método de bolhas 

L = [7,4,3,12,8]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x+1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)

# Python possui um método que ordena rapidamente uma lista

L = [7,4,3,12,8]
L.sorted()
print(L)

# .sorted retorna uma lista ordenada 