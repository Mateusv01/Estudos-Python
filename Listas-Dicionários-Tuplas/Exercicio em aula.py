
def Exercicio():
  L = [1,2,3,4,5]
  x = 0
  while x < len(L):
    print(f"{L[x] **2}")
    x += 1

def exemploappend():    
    L = []
    while True:
        n = int(input("Digite um número ( 0 para sair): "))
        if n == 0:
            break
        L.append(n)
    x = 0
    while x < len(L):
        print(L[x])
        x += 1

def exercicio62():
    primeira = [1]
    segunda = [2]
    terceira = primeira + segunda

    print(terceira)


primeira = [1,2]
segunda = [2,5]
terceira = []

junta = primeira[:]
junta.extend(segunda)
x = 0 
while x < len(junta):
    terceira.append(junta[x])
    x += 1
print(terceira)






duas_listas = primeira[:]
duas_listas.extend(segunda)
while x < len(duas_listas):
    y = 0
    while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break;
        y=y+1
    if y == len(terceira):
        terceira.append(duas_listas[x])
    x=x+1
x=0
while x < len(terceira):
    print("%d: %d" % (x, terceira[x]))
    x=x+1