""" A programação orientada a objetos facilita a escrita e a manutenção de nossos programas
    ultilizando classes e objetos. Classes são a definição de um novo tipo de dados que 
    associa dados e operações em uma só estrutura. Um objeto pode ser entendido como uma
    variável cujo tipo é uma classe, ou seja, um objeto é uma instância de uma classe
    
    
    A programação orientada a objetos é uma técnica de programação que organiza nossos 
    programas em classes e objetos em vez de apenas funções
    
    
    """

# -----------------------------------------------|
#     Objetos como representação do mundo real   |
# -----------------------------------------------|

""" Podemos entender um objeto em Python como uma representação de um objeto
    do mundo real
    
    
    Vejamos um exemplo com um aparelho de televisão, podemos dizer que uma televisão
    tem uma marca e tamanho de tela. Podemos tambem pensar no que podemos fazer com esse
    aparelho exemplo, mudar de canal desligar ou ligar"""


class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 20
        self.marca = "Lg"
tv = Televisão() # 5 

print(tv.ligada)
print(tv.canal)

tv_sala = Televisão()
tv_sala.ligada = True
tv_sala.canal = 3
print(tv.canal)
print(tv_sala.canal)


tv.tamanho = 68
tv.marca = "Samsung"

tv_sala.tamanho = 30
tv_sala.marca = "Lg"

print(f"tv tamanho: {tv.tamanho} tv marca: {tv.marca}")
print(f"tv sala tamanho: {tv_sala.tamanho} tv marca {tv_sala.marca}")


""" O método __init__ sempre será executado no começo dos objetos, sendo por isso
    chamado de método construtor (constructor) ou iniciador
    
    self.ligada é um valor de self , ou seja, do objeto Televisão. Todo método em Python
    tem o self como primeiro parâmetro
    
    Observe tambem que escrevemos self.canal para criar um atributo, e não uma simples variável
    local

    Em 5 criamos o objeto tv ultilizando a classe Televisão, Dizemos que tv é agora um objeto
    de classe Telvisão ou que tv é uma instância de Televisão 

    Observe que ao imprimir o canal de cada televisão temos valores independentes, pois a tv e tv_sala
    são dois objetos independentes 


    A caracteristica de quando criamos um objeto de uma classe, ele tem todos os atributos e métodos que especificamos
    ao declarar a classe, isso simplifica o desenvolvimento dos programas, pois podemos definir
    o comportamento de todos os objetos de uma classe(métodos), preservando os valores individuais
    de cada um (atributos) 


    """

""" Agora veremos como associar um comportamento à classe Televisão 
    Definindo dois métodos muda_canal_para_cima e muda_canal_para_baixo"""


class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1

tv = Televisão()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()

print(f"Mudança de 2 pra cima: {tv.canal}")

tv.muda_canal_para_baixo()

print(f"Mudança de um pra baixo {tv.canal}")


# -------------------------------|
#     Passagem de Parâmetros     |
# -------------------------------|

""" Um problema com a classe televisão é que não controlamos os limites
    dos nossos canais. Podendo obter canais negativos ou números muito grandes
    Vamos modificar o construtor para obter o valor mínimo e máximo"""

class Televisão:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin


tv = Televisão(2, 10)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)


""" Isolamos os detalhes do funcionamento da classe do resto do programa 
    Esse efeito é chamado de encapsulamento. Dizemos que uma classe deve
    encapsular ou ocultar detalhes do seu funcionamento, máximo possível
    No caso dos métodos para mudar o canal, incluímos a verificação sem
    alterar o resto do programa"""


# Exercício 10.2 

""" Adicionar mais uma preposição no escopo (canal_inicial) """

# Exercício 10.3

""" Ao trabalharmos com classses e objetos, assim como fizemos ao estudar funções,
    precisamos representar em Python uma abstração do problema. Quando realizamos
    uma abstração, reduzimos os detalhes do problema ao nessessário para sulucioná-lo
    Estamos contruindo um modelo, ou seja, modelando nossas classes e objetos"""



""" Tudo que aprendemos com funções é também válido para métodos. A principal diferença
    é que um método é assiociado a uma classe e atua sobre um objeto. O primeiro parâmetro
    é o self, por meio dele que teremos acesso aos outros métodos de uma classe
    Você não precisa passar o objeto como primeiro parâmetro ao invocar um método
    O Python já faz isso automáticamente"""


# Exercício 10.4 

""" Só limitar os valores 

class Televisão:
    def __init__(self, min = 2, max = 14):

        """

# Exercício 10.5

""" Adcicionar objetos limitantes no final

tv = Televisão(min=1, max=22)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)

tv2 = Televisão(min=2, max=64)
tv2.muda_canal_para_baixo()
print(tv2.canal)
tv2.muda_canal_para_cima()
print(tv2.canal)

"""