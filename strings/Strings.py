# conceito de len (conta o número de caracteres numa sentença)

from re import X


print(len("a"))
print(len("ab"))
print(len(""))
print(len("o rato roeu a roupa"))


# testes de índice Strings

a = "ABCDEF"

print(a[0])
print(a[1])
print(a[5])


print(len(a))

# Operação com Strings

# Concatenação

s = "ABC"
print(s + "C")

print(s + "D" * 4)

print("8" + "-" * 10 + ">)")

# Composição

# Marcadores
# %d = Números inteiros
# %s = Strings
# %f = Números decimais

idade = 22
print("[%d]" % idade)

print("[%03d]" % idade)

print("[%3d]" % idade)

print("[%-3d]" % idade)

#Para colocar a vírgula

print("%5f" % 5)

print("%5.2f"% 1200)

# O poder real da composição de strings

print("%s tem %d anos e apenas R$%5.2f no bolso" % ("João", 22, 51.34))

# .Format (forma mais moderna doq usar %)

print("{} tem {} anos e apenas R${} no bolso".format("João", 22 , 51.34))

# f-strings (forma moderna da versão 3.6)

nome = "João"
grana = 51.34


print(f"{nome} tem {idade} anos e apenas R$ {grana} no bolso")

# Fatiamento de Strings 

s = "ABCDEFGHI"
print(s[0:2])

print(s[1:2])

print(s[0:5])

print(s[1:8])

# Testes com negativo

print(s[0:-2])

print(s[0:-4])

print(s[0:-1])

print(s[-2:-1])

# sendo que ABCDEFGH
     #1,2,3,4,5,6,7,8 E
     #-1,-2,-3,-4,-5,-6,-7,0