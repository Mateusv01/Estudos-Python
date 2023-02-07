


distância = int(input("Digite a distância da viagem: "))

conta1 = distância * 0.50
conta2 = distância * 0.45

if distância > 200:
    print(f"O preço da viagem vai ser de R$: {conta2}")
else:
    print(f"O preço da viagem vai ser de R$: {conta1}")



# Programa Categoria x Preço

categoria = int(input("Digite a categoria do produto (1 a 5):  "))
if categoria == 1:
    preço = 10
    print (F"{preço} R$")
else:
    if categoria == 2:
        preço = 18
        print(F"{preço} R$")
    else:
        if categoria == 3:
            preço = 23
            print(F"{preço} R$")
        else:
            if categoria == 4:
                preço = 26
                print(F"{preço} R$")
            else:
                if categoria == 5:
                    preço = 31
                    print(F"{preço} R$")
                else:
                    print("Categoria incorreta, digite um número válido")
                    preço = 0
                    

            
            
            