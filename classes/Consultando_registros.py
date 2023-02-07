""" Primeiro vamos ultilizar uma variação de comando select para mostrar apenas alguns registros
    implementando uma seleção de registros com base em uma pesquisa. Pesquisas em SQL são feitas
    com a cláusula where. 
    
    
 w   select * from agenda where nome = "Mateus"
    
    Veja que apenas adicionamos uma cláusula após o nome da tabela. O critério deve ser escrito em uma expressão
    como: nome = "Mateus" 

    
    """

# Consulta com filtro de seleção
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from agenda where nome ='Mateus'")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome {resultado[0]}\nTelefone: {resultado[1]}")


""" Veja que escrevemos 'Mateus' entre apóstrofos. Aqui podemos usar um pouco que já sabemos de Python
    e escrever
    
    cursor.execute('select * from agenda where nome = "Mateus"')
    ou  """
    #cursor.execute("""select * from agenda where nome = "Mateus" """)

nome = input("Nome a selecionar: ")
with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor) as cursor:
        cursor.execute(f'select * from agenda where nome = "{nome}"')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
print(f"Nome {resultado[0]}\nTelefone: {resultado[1]}")


