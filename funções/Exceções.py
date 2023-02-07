""" Exceções são situações inesperadas em nosso código 
    Alguns tipos de exceções são ValueError, quando tentamos converter uma letra em número
    IndexError, quando tentamos acessar os elementos de uma lista além do seu tamanho"""

""" O BLOCO RESPONSÁVEL POR TRATAR EXCEÇÕES É O try"""

nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um Número!")
    except IndexError:
        print("Valor inválido, digite entre -3 e 3")



""" O bloco try permite delimitar o código que pode gerar uma exceção, ou seja
    A tentativa pode levar ao erro, por isso try vem junto com o except, se nenhum
    erro ocorrer, o except nem será executado"""


nomes2 = ["Juan", "Yuri", "Alberto"]
for tentativa2 in range(3):
    try:
        f = int(input("Digite o índice que quer imprimir: "))
        print(nomes2[f])
    except Exception as e:
        print(f"Algo de errado aconteceu: {e}")

""" O mesmo bloco try pode ter vários except, além disso no final pode ter uma declaração finally 
    Assim estamos colocando que o código seja executado mesmo que aconteça uma exceção sem nenhum filtro"""


# Outra versão do mesmo programa mas que trata apenas a exceção

nomes2 = ["Juan", "Yuri", "Alberto"]
for tentativa2 in range(3):
    try:
        f = int(input("Digite o índice que quer imprimir: "))
        print(nomes2[f])
    except ValueError as e:
        print(f"Digite um número")
    finally:
        print(f"Tentativa{tentativa2 + 1}")


""" Exceções são um recurso bem popular em várias linguagens de programação, sua maior vantagem é separar
    Uma execução normal de uma execução anormal
    Usando exceções, evitamos retornar e verificar códigos de erro a cada chamada 
    Sendo melhor para o tratamento de erros"""

""" Podemos gerar exceções com o usando a intrução raise"""

nomes = ["Renato", "Augusto", "Roger"]
try:
    i = int(input("Digite o índice que quer imprimir: "))
    print(nomes[i])
except ValueError as e:
    print("Digite um número")
    raise
finally:
    print("O finally sempre é executado")


def épar(n):
    try:
        return n % 2
    finally:
        print("Executado antes de retornar")
try:
    print(2, épar(2))
    print("A",épar("A"))
except Exception:
    print("Algo de errado aconteceu")


""" Ultilizando o raise, podemos também criar nossas próprias exceções"""



def épar2(n):
    try:
        return n % 2
    except Exception:
        raise ValueError("Valor inválido")

""" Nesse caso a exceção original também foi reportada e em primeiro lugar, caso não seja o efeito desejado use:"""

def épar2(n):
    try:
        return n % 2
    except Exception:
        raise ValueError("Valor inválido") from None


""" O bloco try também possui uma declaração else, assim como o while e for
    A declaração else é executada apenas se não houver exceção no try e pode ser combinada
    Com o except e finally"""


while True:
    try:
        v = int(input("Digite um número inteiro (0 sai): "))
        if v == 0:
            break
    except Exception:
        print("Valor inválido, Redigite")
    else:
        print("Parabéns nenhuma exceção pra você")
    finally:
        print("Executado sempre, mesmo com break")