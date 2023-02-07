# Sequências e tempo

# Programa - Exemplo de sequência e tempo

dívida = 0
compra = 100
dívida = dívida + compra
compra = 200
dívida = dívida + compra
compra = 300
dívida = dívida + compra
compra = 0

print(dívida)

# Rastreamento
# Entender a lógica do programa por meio de um rastreamento feito á lápiz para compreender como seu programa realmente funciona #

# Entrada de dados 

# input

x = input("Digite seu nome")

print("Olá" + x )

# conversão de entrada de dados

anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bônus = anos * valor_por_ano

print(f"Bônus de R$ {bônus:5.2f}")