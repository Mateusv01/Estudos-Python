# Contagem regressiva
x = 10

while x >= 0:
    print(x)
    x = x - 1
print("Fogo!")
# Contagem até 100

y = 1
while y <= 100:
    print(y)
    y = y + 1

z = 50
while z <= 100:
    print(z)
    z = z + 1

pontos = 0 
questão = 1

while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and resposta == "b" or "B":
        pontos = pontos + 1 
    if questão == 2 and resposta == "a" or "A":
        pontos = pontos + 1 
    if questão == 3 and resposta == "d" or "D":
        pontos = pontos + 1 
    questão = questão + 1
    print(pontos)
print(f"O aluno fez {pontos} pontos(s)")