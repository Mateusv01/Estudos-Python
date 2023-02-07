numero = int(input("Digite um número: "))

if numero <  0:
    print("Digite um número válido ")
if numero == 0 or numero == 1:
    print("Não são primos")

else:
    if numero == 2:
        print("O número 2 é primo")
    elif numero%2 == 0:
        print("não é primo, pois 2 é o único número par primo.")
    else:
        x = 3
        while x<numero:
            if numero % x == 0:
                break
            x = x + 2
        if x == numero:
            print("%d é primo" % numero)
        else:
            print("%d não é primo, pois é divisível por %d" % (numero, x))
    