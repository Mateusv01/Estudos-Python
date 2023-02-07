""" Já sabemos como criar tabelas, inserir registros e fazer consultas simples. Vamos
começar a usar o comando update para alterar nossos registros.


    update agenda set telefone = "1234-2133" where nome = 'Mateus'


A claúsula where funciona como no comando select, ou seja, ela avalia uma expressão lógica que, quando
verdadeira, inclui o registro na lista de registros a modificar. A segunda parte do comando update é a
cláusula set. Essa cláusula é usada para indicar o que fazer nos registros selecionados pela expressão
do where. No exemplo, set telefone = "" muda o conteúdo do campo telefone para o número indicado.

O comando inteiro pode ser lido como, atualize os registros da tebela agenda, alterando o telefone em todos os
registros com nome Mateus
 

"""
import sqlite3
from contextlib import closing
#with sqlite3.connect("agenda.db") as conexão:
 #   with closing(conexão.cursor()) as cursor:
  #      cursor.execute("""update agenda
   #                         set telefone = '12345-6789'
    #                        where nome = 'Mateus' """)
    #conexão.commit

"""
Nesse exemplo usamos constantes, logo não precisamos usar parâmetros. As mesmas regras que aprendemos
para o comando select se aplicam no comando update. Se os valores não forem constantes, precisa usar 
parâmetros

Se a cláusula where for retirada do comando, todos os registros de telefone serão modificados


Vamos usar a propridade rowcount de nosso cursor para saber quantos registros foram alterados pelo
nosso update 
"""

# Programa 11.6 - Exemplo de update sem where e com rowcount

with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("""update agenda
                            set telefone = '12345-6789' """)
        print("Registros alterados: ", cursor.rowcount)


""" Após modificar o banco de dados precisamos chamar o método commit para salvar os registros

A propriedade rowcount é muito interessante para confirmarmos o resultado de comandos de atualização, como update.
Essa propriedade não funciona com select, retornando sempre -1
No caso de update, poderíamos fazer uma verificação de quantos registros seriam alterados antes de chamarmos o
commit: 
"""

with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("""update agenda
                            set telefone = '12345-6789' """)
        print("Registros alterados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexão.commit()
            print("Alterações gravadas")
        else:
            conexão.rollback()
            print("Alterações abortadas")



"""
O método rollback faz o inverso do commit, abortando as alterações e deixando o banco de dados como antes.
Os métodos commit e rollback fazem o controle de transações do banco de dados

Podemos entender uma transação como um conjunto de operações que deve ser executado completamente. Isso significa
que operações que não fazem sentido, salvo se realizadas em um só grupo. Se a execução do grupo falhar, todas
as alterações causadas durannte a transação corrente devem ser revertidas
"""

# Programa 11.5 aumentando preço dos produtos preço.db

#with sqlite3.connect("preço.db") as conexão:
 #   with closing(conexão.cursor()) as cursor:
  #      cursor.execute("""update preço
   #     cursor.execute('''select * from preço''')
    #       print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))


with sqlite3.connect("preço.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        nome = input("Digite o nome do produto a alterar o preço: ")

        cursor.execute('''select * from preço
                          where nome = ?''', (nome,))

        resultado = cursor.fetchone()
        if resultado:
            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))
            novo_preço = input("Digite o novo preço: ")
            cursor.execute('''update preço
                              set preço = ?
                              where nome = ?''', (novo_preço, nome))
        else:
            print("Não encontrado.")