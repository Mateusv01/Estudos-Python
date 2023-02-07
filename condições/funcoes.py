# Escreva uma função que retorne o maior de dois numeros

def num_max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(num_max(2,4))


# escreva uma função que receba dois numeros e retorne True se o primeiro for multiplo do segundo

def mult(a,b):
    return a % b == 0


print(mult(4, 2))

def area_quadrado(lado):
    return lado ** 2
    

print(area_quadrado(4))


def area_triangulo(base,altura):
    return (base * altura) / 2

print(area_triangulo(2, 5))