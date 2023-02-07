quantidade_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
quantidade_de_anos = int(input("Digite a quantidade de anos que já fumou: "))

contador_em_minutos = quantidade_de_anos * 345 * quantidade_por_dia * 10

contador_em_dias = contador_em_minutos / (24 * 60)

print (f"Dias de vida que você perdeu = {contador_em_dias} dias")