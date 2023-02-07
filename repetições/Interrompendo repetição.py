
n = 0
x = 0
while True:
    p = int(input("Digite um numero para somar e (0) para sair: "))
    if p == 0:
        break
    n+=p
    x+=1
print(f"Quantidade de números digitados: {x}")
print(f"Soma: {n}")
print(f"Média: {n/x}")