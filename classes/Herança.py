""" A herança cria subclasses de um objeto no qual vira uma superclasse
    a vantagem de usar herança é poder modificar a superclasse sem nenhum 
    medo pois ela se ajusta corretamente 
    
    É importante notar que ao usarmos herança, as subclasses devem poder substiituir suas superclasses
    sem perda de funcionalidade e sem gerar erros nos programas 
    
    
    
    
    class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo) ------------> Herança
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo = valor
            self.operações.append(["Saque", valor]) """