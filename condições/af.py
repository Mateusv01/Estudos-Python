# Tradutor
# Toda vogal é transformada em g

def tradutor(frase):
    traducao = ""
    for letra in frase:
        if letra in "AEIOUaeiou":
            traducao = traducao + "g"
        else:
            traducao = traducao + letra
    return traducao

print(tradutor(input("Digite sua frase: ")))