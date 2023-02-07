divisor = int(input("Digite o divisor: "))
dividendo = int(input("Digite o dividendo: "))

quociente = 0 

x = dividendo

while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x 
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")


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
print(f"O aluno fez {pontos} pontos(s)")
