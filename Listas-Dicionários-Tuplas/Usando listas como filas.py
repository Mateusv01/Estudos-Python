# Para criar uma fila em Python basta imaginar uma lista como uma fila, o primeiro a chegar será atendido
# enquanto o último poderá ser adicionado pelo método pop nessa fila
# DIZEMOS QUE O PRIMEIRO A CHEGAR É O PRIMEIRO A SAIR
# FIFO (FIRST IN FIRST OUT)

# Programa 6.7 - Simulação de uma fila de banco

último = 0
filaA = []
filaB = []
while True:
    print(f"\nExistem {len(filaA)} clientes na fila")
    print(f"Fila atual: {filaA}")
    print(f"Fila atual: {filaB}")
    print(f"Digite F para adicionar um cliente a primeira fila e R para adicionar a segunda\nOu A para realizar o atendimento")
    print("na primeira fila e P na segunda. S para sair")
    operação = input("Operação(F,R,A,P ou S): ")
    if operação == "A":
        if len(filaA) > 0:
            atendido = filaA.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia!")
    elif operação == "FFFAAAS":
        último += 3
        filaA.append(último)
        atendido = filaA.pop(0)
    elif operação == "P":
        if len(filaB) > 0:
            atendido = filaB.pop(0)
            print(f"Cliente {atendido} atendido")
    elif operação == "R":
        último += 1 
        filaB.append(último)
    elif operação == "F":
        último += 1 
        filaA.append(último)
    elif operação == "S":
        break
    else:
        print("Operação inválida")