quantidade = int(input("Digite a quantidade de Kwh consumidos: "))
tipo = str(input("Digite qual o tipo de instalação ( R , I , C): "))



if tipo == "R" and quantidade <= 500:
    preço = 0.40
elif tipo == "R" and quantidade > 500:
    preço = 0.65
elif tipo == "I" and quantidade <= 1000:
    preço = 0.55
elif tipo == "I" and quantidade > 1000:
    preço = 0.60
elif tipo == "C" and quantidade <= 5000:
    preço = 0.55
elif tipo == "C" and quantidade > 5000:
    preço = 0.60
else:
    print("Tipo de instalação incorreta")

calculo = preço * quantidade
print (f"Preço: {preço} ")
print (f"Valor a ser pago R$: {calculo}")