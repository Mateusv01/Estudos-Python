# Uma pilha tem uma política de acesso bem definida, novos elementos são adicionados ao topo
# Dizemos que o ÚTIMO A CHEGAR É O PRIMEIRO A SAIR
# LIFO (LAST IN FIRST OUT)

# Programa 6.8 - Pilha de pratos

prato = 5
pilha = list(range(1,prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"pilha atual: {pilha}")
    print(f"Digite E para empilhar um novo prato,\nou D para desempilhar.S para sair")
    operação = input("Operação(E,D ou S): ")
    if operação == "E":
        prato += 1 # novo prato adicionado
        pilha.append(prato)
    elif operação == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia!")
    elif operação == "S":
        break
    else:
        print(f"Operação ínvalida, digite entre (E,D ou S)") 


expressão = input("Digite a sequência de parênteses a validar:")
x=0
pilha2 = []
while x<len(expressão):
    if(expressão[x] == "("):
        pilha2.append("(")
    if(expressão[x] == ")"):
        if(len(pilha2)>0):
            topo = pilha2.pop(-1)
        else:
            pilha2.append(")")  # Força a mensagem de erro
            break
    x=x+1
if(len(pilha2)==0):
    print("OK")
else:
    print("Erro")











