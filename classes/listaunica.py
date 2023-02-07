""" Nos exemplos anteriores não fizemos nenhuma verificação quanto
    a duplicidade dos valores. Por exemplo, uma lista de clientes 
    em que dois clientes são a mesma pessoa seria aceita sem problemas.
    Outro problema de nossa lista simles é que ela não verifica se os
    elementos são objetos da classe Cliente.
    Vamos modificar isso construindo uma nova classse, chamada ListaÚnica"""

class ListaÚnica:
    def __intit__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class
    def __len__(self):
        return len(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getitem__(self, p):
        return self.lista[p]
    def indiceVálido(self, i):
        return i >= 0 and i < len(self.lista)
    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)
    def remove(self, elem):
        self.lista.remove(elem)
    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1
    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_class):
            raise TypeError("Tipo inválido")
    def ordena(self, chave=None):
        self.lista.sort(key=chave)


lu = ListaÚnica()
lu.adiciona(4)
print(len(lu))


""" O método __len__ é responsável por retornar um número de elementos a partir do self.lista
    o método __iter__ simplismente chama uma função iter do python com nossa lista interna self.lista
    o método __getitem__ que recebe o valor índice (p) e retorna o elemento correspondente em nossa lista
    
    O Python possui vários métodos mágicos, métodos especiais que tem o formato __nome__. Os métodos
    permitem dar outro comportamento a nossas classes e usá-las quase como classes da própria 
    linguagem. A ultilização dos métodos mágicos não é obrigatória mas ajuda muito na construção
    dos programas

    O __eq__ é o método especial ultilizado para comparações de igualdade (==) de nossos objetos

    O método __neq__ (!= not equal) é a mesma coisa

    e __lt__ (< less than)

    __gt__ (> greater than)

    Recurso Decorators:
        o primeiro decoradorr @total_ordering é definido no módulo functools, por isso temos que 
        importar em nosso programa, ele implementa todos os métodos de comparação especiais
        (== >= <= > < !=)

        Outro decorador é @staticmethod, esse decorador cria um método estático, isto é, um método
        que pode ser apenas com o nome da classe

    
"""