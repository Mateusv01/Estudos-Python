# Programa Categoria x Preço feito por elif

categoria = int(input("Digite a categoria do produto (1 a 5):  "))
if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31

else:
    print("Número incorreto, digite um número válido")
    preço = 0

print(f"O preço do produto é: R${preço:6.2f}")