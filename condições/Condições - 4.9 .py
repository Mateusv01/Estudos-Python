valor = int(input("Digite o valor da casa que deseja comprar: "))
salario = float(input("Digite seu salário: "))
anos_a_pagar = int(input("Digite a quantidade de anos que pretende pagar: "))

prestação = (valor / anos_a_pagar) / 30

salario_30 = salario - (salario * 30 ) / 100

if prestação > salario_30:
    print("A prestação não pode ser maior que 30 porcento do salário")
else:
    print(f"Valor mensal da prestação é de R$: {prestação}")
    