""" Um banco de dados pode realizar operações de agrupamento de dados facilmente. Podemos, por exemplo, solicitar o valor
mínimo de um grupo de registros, assim tambem o máximo ou a média desses valores 

Vejamos como realizar um grupo simples e exibir quantos registros fazem parte desse grupo, usado a função count. A cláusula 
SQL que indica agrupamento é o group by, seguida do nome dos campos que compõe o grupo.

Imagine que o banco vai concatenar cada um desses campos, criando um valor para cada registro. Vamos chamar esse valor de 
"chave de grupo". Todos os registros com a mesma chave de grupo fazem parte do mesmo grupo e serão representados por apenas um registro
na consulta de seleção. Essa consulta com grupo só pode conter os campos ultilizados para compor a chave do grupo e funções de 
agrupamento de dados, como min(mínimo), max(máximo), avg(média), sum(soma) e count(contagem)

Esse comando ultiliza a cláusula group by região para especificar a chave de grupo. Dessa forma, todos os registros que pertecem
a mesma região são agrupados

"""
import sqlite3
print("Região Número de Estados")
print("======== ================")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
        select região, count(*)
        from estados
        group by região"""):
        print("{0:6} {1:17}".format(*região))

""" Vamos adicionar as funções min,max,avg,sum no campo população"""

print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
        select região, count(*), min(população),
                max(população), avg(população), sum(população)
        from estados
        group by região"""):
         print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))
    print ("\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
        *conexão.execute("select count(*), min(população), max(população), avg(população), sum(população) from estados").fetchone()))

""" Conseguimos calcular a populaçao mínima, máxima, média e total de cada região
    Veja que na segunda consulta que calcula os dados para o Brasil, não foi colocado o group by, assim fazendo que todas
    façam parte de um mesmo grupo 
    
    
    Ao ultilizarmos as funções de agregação e a cláusula group by, podemos continuar usando tudo que já aprendemos em SQL,
    como as cláusulas where e order by
    
    """

print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
        select região, count(*), min(população),
               max(população), avg(população), sum(população) as tpop
        from estados
        group by região
        order by tpop desc"""):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))
    print ("\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
        *conexão.execute("""
            select count(*), min(população), max(população),
                   avg(população), sum(população) from estados""").fetchone()))
print(" " *20)

""" Apenas adicionamos a linha order by sum(população) desc no final de nossa consulta
    Podemos usar a cláusula as do SQL para dar nomes as colunas de uma consulta. Veja a consulta
    modificada para usar as e criar uma coluna tpop para a soma da população:

        select região, count(*), min(população), max(população), avg(população),
            sum(população) as tpop
        from estados group by região 
        order by tpop desc

    Veja que escrevemos sum(população) as tpop, dando o nome tpop a soma. Depois, ultilizamos o nome tpop 
    na cláusula do order by. Esse tipo de construção evita a repetição da função na consulta e facilita a leitura
    """

print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
        select região, count(*), min(população),
               max(população), avg(população), sum(população) as tpop
        from estados
        group by região
        order by tpop desc"""):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))
    print ("\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
        *conexão.execute("""
            select count(*), min(população), max(população),
                   avg(população), sum(população) from estados""").fetchone()))
print("" * 90)
""" Podemos também filtrar os resultados após o agrupamento, usando a cláusula having. Para entender a
diferença entre while e having. Where é executada antes do agrupamento, selecionando os registros que faram
parte do resultado do agrupamento e decide quais faram parte do resultado final


    select região, count(*), min(população),
    from estados group by região
having count(*) > 5
        order by tpop desc
        
        
        Programa inteiro usando having"""

print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
        select região, count(*), min(população),
               max(população), avg(população), sum(população) as tpop
        from estados
        group by região
        having count(*)>5
        order by tpop desc"""):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))