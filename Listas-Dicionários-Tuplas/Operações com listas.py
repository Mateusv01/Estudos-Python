# Podemos percorrer listas de forma a verificar o número maior e menor

# 6.11 - Verificação de maior ou menor valor

L = [1,7,2,4]
menor = L[0]
maior = L[0]
for e in L:
    if e < menor:
        menor = e
    elif e > maior:
        maior = e

print(menor)
print(maior)

# Exercício 6.13

T = [-10,-8,0,1,2,5,-2,-4]
temperatura_maior= T[0]
temperatura_menor= T[0]
média = 0
for r in T:
    if r < temperatura_menor:
        temperatura_menor = r
    if r > temperatura_maior:
        temperatura_maior = r 
    média = média + r
print(f"Temperatura maior: {temperatura_maior} \n Temperatura menor: {temperatura_menor} \n Média: {média / len(T)} ")



# -------------------------------------|
#           APLICAÇÕES                 |
# -------------------------------------|


# Fazendo a separação das listas de pares e ímpares

V = [9,8,7,12,0,13,21]
P = []
I = []
for e in V:
    if e % 2 ==0:
        P.append(e)
    else:
        I.append(e)
print(f"Pares: {P}")
print(f"Ímpares: {I}")


# Programa da ultilização de salas de cinema no qual os lugares vagos são preenchidos para a venda

lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos)"))
        if lugares > lugares_vagos[sala - 1]:
            print("Essse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
        print("Ultilização de salas")
        for x,l in enumerate(lugares_vagos):
            print(f"Sala{x + 1} - {l} lugare(s) vazio(s)")