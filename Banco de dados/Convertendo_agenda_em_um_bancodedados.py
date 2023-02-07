""" Converter a agenda  para um banco de dados vai levar enfrentar o problema de mapeamento de objetos
e os bancos de dados relacionais, como SQLite.
Um dos maiores problemas nesse mapeamento é manter os dados do programa e banco de dados sincronizados
Existe uma biblioteca especial para resolver esse tipo de problema, usando o Mapeamento Objeto Relacional 
(Object Relational Mapping, ORM).

Primeiramente vamos cirar uma subclasse de ListaÚnica para controlar os registros apagados de nossas listas
Depois, vamos criar métodos em uma outra classe chamada DBagenda, responsável por manter o banco de dados e
executar as operações da agenda. 

"""
from AppAgenda import *
class DBListaÚnica(ListaÚnica):
    def __init__(self, elem_class):
        super().__init__(elem_class)
        self.apagados = []

    def remove(self, elem):
        if elem.id is not None:
            self.apagados.append(elem.id)
        super().remove(elem)

    def limpa(self):
        self.apagados = []

class DBNome(Nome):
    def __init__(self, nome, id_=None):
        super().__init__(nome)
        self.id = id_

class DBTipoTelefone(TipoTelefone):
    def __init__(self, id_, tipo):
        super().__init__(tipo)
        self.id = id_

class DBTelefone(Telefone):
    def __init__(self, número, tipo=None, id_=None, id_nome=None):
        super().__init__(número, tipo)
        self.id = id_
        self.id_nome = id_nome

class DBTelefones(DBListaÚnica):
    def __init__(self):
        super().__init__(DBTelefone)

class DBTiposTelefone(ListaÚnica):
    def __init__(self):
        super().__init__(DBTipoTelefone)

class DBDadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = DBTelefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if type(valor)!=DBNome:
            raise TypeError("nome deve ser uma instância da classe DBNome")
        self.__nome = valor

    def pesquisaTelefone(self, telefone):
        posição = self.telefones.pesquisa(DBTelefone(telefone))
        if posição == -1:
            return None
        else:
            return self.telefones[posição]


""" A classe DBListaÚnica herda a classe ListaÚnica e sua pricipal função é manter uma lista de id apagados
Isso vai permitir apagar elemenos das listas, e do banco de dados. A classe DBListaÚnica só pode trabalhar 
com classes que possuam um atributo id


As classes DBNome e DBtelefone derivam de nome e telefone. A diferença é que eles agoras incluem o 
atributo id 

A classe DBDadosAgenda modificam o tipo de lista telefones de Telefones para DBTelefones
"""