# -------------------------------------|
#          Listas com strings          |
# -------------------------------------|


# Exemplo de listas usando strings

S = ["maçãs", "peras", "kiwis"]
print(len(S))
S[0] = "maçãs"

# Um programa mais complexo de uma lista de compras, que imprime uma lista até que seja digitado fim

compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    compras.append(produto)
for p in compras:
    print(p)

# -------------------------------------|
#       Listas dentro de listas        |
# -------------------------------------|

# Podemos acessar as strings dentro da lista, letra por letra, segundo o índice 


S = ["abacaxi", "pera"]

print(S[0][0])
# a
print(S[1][1])
# p

# Ou usando um programa 

L = ["maçãs","peras","kiwis"]
for s in L:
    for letra in s:
        print(letra)


# Listas com elementos de tipos diferentes 

produto1 = ["maça", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]

# Assim produto1,2 e 3 seriam três listas com três elementos cada uma 

# listas de listas

compras = [produto1,produto2,produto3]
print(compras)

# Agora temos uma lista chamada de compras, também com três elementos que são uma lista a parte
# Para imprimir essa lista

for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]}")

# Um programa que é capaz de perguntar o nome do produto, quantidade e preço, no final imprimir uma lista completa

compras = []
while True:
    adicionar = input("Produto: ")
    if adicionar == "fim":
        break
    quantidade = int(input("Quantidade: "))
    preço = float(input("Preço: "))
    compras.append([adicionar,quantidade,preço])
soma = 0.0
for elemento in compras:
    print(f"{elemento[0]} x {elemento[1]} {elemento[2]} {elemento[1] * elemento[2]}")
    soma += elemento[1] * elemento[2]
print(f"Total: {soma}")