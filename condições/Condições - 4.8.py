primeiro = int(input("Digite um número: "))
segundo = int(input("Digite um número: "))
operador = str(input("Coloque o operador desejado ( + , - , * , /): "))

if operador == "+":
    conta = primeiro + segundo
elif operador == "-":
    conta = primeiro - segundo
elif operador == "*":
    conta = primeiro * segundo
elif operador == "/":
    conta = primeiro / segundo
else:
    print ("Sentença incorreta, coloque um número válido")
print (f"Sua conta deu: {conta}")