from re import A


velocidade = int(input("Digite sua velocidade: "))

multa = (velocidade - 80) * 5

if velocidade > 80:
    print(f"Você foi multado em R$: {multa} reais")
if velocidade <= 80:
    print("Velocidade permitida")


# 3 números e imprima o maior e menor

a = int(input("Digite um número: "))
b = int(input("Digite um outro número: "))
c = int(input("Digite um outro número: "))

if a>b and a>c and c>b:
    print("O primeiro é maior e o segundo menor")
elif a>b and a>c and b>c:
    print("O primeiro é maior e o terceiro menor ")
elif b>a and b>c and a>c:
    print("O segundo é maior e o terceiro menor ")
elif b>a and b>c and c>a:
    print("O segundo é maior e o primeiro menor ")
elif c>b and c>a and a>b:
    print("O terceiro é maior e o segundo menor ")
elif c>b and c>a and b>a:
    print("O terceiro é maior e o primeiro menor ")



#calcular o valor de aumento do salário

salario = float(input("Digite seu salário em R$: "))
aumento10 = salario + (salario * 10) /100
aumento15 = salario + (salario * 15) /100

if salario > 1250.00:
    print(f"Seu novo salário é de R$: {aumento10:6.2f}")
else:
    print(f"Seu novo salário é de R$: {aumento15:6.2f}")