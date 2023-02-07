# Podemos pesquisar se um elemento está ou não em uma lista, verificando do primeiro ao último

# Programa 6.9 - Pesquisa sequencial

L = [15,7,27,39]
p = int(input("Valor a procurar:"))
v = int(input("Segundo valor a procurar:"))
x = 0
achouP = -1 # Não encontramos o valor
achouV = -1
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = x
    if L[x] == v:
        achouv = x
    x += 1
if achouP !=-1:
    print(f"{p} achado na posição {x}")    
else:
    print(f"{p} não encontrado")
if achouV !=-1:
    print(f"{v} achado na posição {x}")
else:
    print(f"{v} não encontrado")
if achouP !=-1 and achouV !=-1:
    if achouP <= achouV:
        print("v foi achado antes que o p")
    else:
        print("p foi achado antes de v")

