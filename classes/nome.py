from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self, nome):
        if nome is None or not nome.strip():
            raise ValueError("Nome não pode ser nulo e nem em branco")
        self.nome = nome
        self.chave = nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return (f"<Classe {type(self).__name__} em 0x {id(self):x} Nome: {self.nome} Chave: {self.chave}>")
    def __eq__(self, outro):
        print("__eq__ Chamando")
        return self.nome == outro.nome
    def __lt__(self, outro):
        print("__lt__ Chamado")
        return self.nome < outro.nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if valor is None or not valor.strip():
            raise ValueError("Nome não pode ser nulo ou em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()





A = Nome("Mateus")

print(A)

# B = Nome("")
# print(B)

A

print(A == Nome("Mateus"))

print(A != Nome("Mateus"))

print(A < Nome("Mateus"))

print(A >= Nome("Mateus"))

print(A.CriaChave("C"))

C = Nome("Teste")

""" Resumo do código e suas ultilidades

    
     O decorador @property, transforma o método nome na propriedade sempre que chamarmos objeto.("nome")
    que retorna self.__nome

    Já o segundo decorador, @nome.setter, transforma o método nome na propriedade usada para alterar o valor 
    de __nome Dessa forma, quando escrevermos objeto.nome = valor, esse método será chamado para efetuar
    as alterações

    Outro detalhe importante é que acrescentamos duas sublinhas (__) antes do nome e chave, fazendo-os
    __nome e __chave. Dessa forma, __nome e __chave ficam escondidos quando acessados fora da classe. Esse
    "esconder" é apenas um detalhe da implementação do Python, que modifica o nome desses atributos de forma
    a torna-los inascessíveis (name mangling)







"""

from nome import Nome

M = Nome("Messi")

print(M)
#print(M.__chave)
M
#print(M.__nome)

""" Quando um programador marcar o atributo com __, está dizendo para não usar fora da classe, salvo
    se tiver certeza do que está fazendo
    
    
    
    Você pode criar atributos que podem ser lidos definindo apenas o método de acesso com @property
    Em nosso exemplo, @nome.setter é que permite alterarmos o nome. Se não ultilizassemos @nome.setter
    o nome seria acessível apenas para leitura
    
    Vejamos como isso funciona no programa 10.2 """
    

from nome import *
L = Nome("Nilo")
L.chave