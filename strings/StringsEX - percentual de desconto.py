preço = int(input("Digite o preço da mercadoria"))

desconto = int(input("Digite o desconto da mercadoria"))

valor_final = preço - (desconto * preço) /100

print(f"Valor do desconto: {desconto}% Valor a pagar: {valor_final}R$") 