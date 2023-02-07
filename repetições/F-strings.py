# Ultilizada na versão mais atualizada do Python

# Podemos formatar as f-strings especificando o número de caracteres

preço = 5.20 

print(f"Preço: {preço:5.2f}") #ou

print (f"Preço: {preço:10.2f}")

print (f"Preço: R${preço:.2f}")

# Pode ser ultilizado o < , > e ^ para alinhar os valores em cima e em baixo

print(f"Preço: R${preço:>10.2f}")
print(f"Preço: R${preço:<10.2f}")
print(f"Preço: R${preço:^10.2f}")

# Podemos especificar qual caractere vai ficar nos espaços em branco

print(f"Preço: R${preço:.^10.2f}")
                        #Só adicionando na frente do :
print(f"Preço: R${preço:x^10.2f}")
                       #^
                       #|
                    # adicionando 

# F-strings podem chamar funções

x = 5.1 
print(f"Inteiro: {int(x)}")

# Assim dá pra fazer operações dentro

print (f"Preço: R${preço * 10:5.2f}!")

#   F-strings também funcionam com strings em múltiplas linhas usando as f"""

print(f"""
...O preço do novo produto é: R${preço:5.2f}
...Pode ser encontrado nas melhores lojas da região
""")

# PARA SEPARAÇÃO DE LINHAS PODEMOS USAR O "\n"

a = "primeira linha\nsegunda linha\nterceira linha\n"

print(a)

print(f"Primeira linha\nSegunda\nTerceira\nQuarta")