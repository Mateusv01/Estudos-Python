distância_percorrida = int(input("Digite a distância percorrida: "))
quantidade_de_dias = int(input("Digite quantidade de dias ultilizados: "))

preço_aluguel = (distância_percorrida * 0.15) + (quantidade_de_dias * 60)

print (f"O preço a se pagar é de: {preço_aluguel}R$")