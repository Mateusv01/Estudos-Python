""" O módulo time traz várias funções para manipular o tempo"""

import time
agora = time.time()
print(agora)
print(time.ctime(agora))

agora2 = time.localtime()
print(agora2)
print(time.gmtime(agora))

""" A função time.time retorna a hora atual em segundos
    No exemplo anterior atribuímos seu resultado a variável
    agora e convertemos em string time.ctime




        Tabela 9.2 - Elementos da tupla de tempo retornada por gmtime

 Posição |  Nome  |  Descrição
    0     tm_year       ano
    1     tm_mon        mês
    2     tm_mday       dia
    3     tm_hour       hora
    4     tm_min        minutos
    5     tm_sec        segundos
    6     tm_wday       dia da semana entre 0,6 sendo que segunda é 0
    7     tm_yday       dia do ano, varia de 1 a 366
    8     tm_isdst      horário de verão, em que 1 indica estar no horário de verão
    
    
    Podemos acessar os dados por nome:
       """

agora3 = time.localtime()
print(f"Ano: {agora3.tm_year}")
print(f"Mês: {agora3.tm_mon}")
print(f"Dia: {agora3.tm_mday}")
print(f"Hora: {agora3.tm_hour}")
print(f"Minutos: {agora3.tm_min}")
print(f"Segundos: {agora3.tm_sec}")
print(f"Dia da Semana: {agora3.tm_wday}")
print(f"Dia no ano: {agora3.tm_yday}")
print(f"Horário de verão: {agora3.tm_isdst}")


""" A função time.strftime permite a formatação do tempo em string.
    você pode assar o formato desejado para string, seguindo os códigos
    de formatação da tabela 9.3


        Tabela 9.3 - Códigos de formatação strftime

  Código |           Descrição            |
    %a      dia da semana abreviado
    %A      nome do dia da semana
    %b      nome do mês abreviado
    %B      nome do mês completo
    %c      data e hora conforme a configuração regional
    %d      dia do mês (01-31)
    %H      hora no formato 24h (00-23) 
    %I      hora no formato 12h
    %j      dia do ano 001-366
    %m      mês(01-12)
    %M      minutos(00-59)
    %p      AM ou PM
    %S      segundos(00-61)
    %U      número da semana(00-53), em que a semana 1 começa após o primeiro domingo
    %w      dia da semana (0,6), em que 0 é domingo
    %W      número da semana (00,53), em que a semana 1 começa após a primeira segunda-feira
    %x      reapresentação regional da data
    %X      reapresentação regional da hora
    %y      ano (00-99)
    %Y      ano com 4 dígitos
    %Z      nome do fuso horário
    %       símbolo de %
    



    Se precisar converter uma tupla em segundos, ultilize a função timegm do módulo calendar
    para trabalhar com data e hora nos programas consultar time,datetime,calendar e locale
"""


# -------------------------------------|
#          Uso de caminhos             |
# -------------------------------------|


""" Uma tarefa comum quando se trabalha com arquivos é manipular caminhos
    O python traz algumas funções interessantes. Aqui veremos as mais importantes
    """
import os.path
caminho = "i/j/k"
print(os.path.abspath(caminho))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
print(os.path.split(caminho))
print(os.path.splitext("arquivo.txt"))
print(os.path.splitdrive("c:/Windows"))

""" A função abspath retorna o caminho absoluto do path passado como parâmetro
    A função basename retorna apenas a última parte do caminho, no exemplo, k
    Já a função dirname retorna o caminho a esquerda da última barra 
    Considere que basename retorna o caminho a direita e dirname a direita

    A função join junta os componentes de um caminho separando-os com barras se nescessário
    Um exemplo:
"""


print(os.path.join("c:", "dados", "programas"))

print(os.path.abspath(os.path.join("c:", "dados", "programas")))


# -----------------------------------------------|
# Visita a todos os subdiretórios recursivamente |
# -----------------------------------------------|



""" A função os.walk facilita a navegação em uma árvore de diretórios. Imagine que
    deseje percorrer todos os diretórios a partir de um inicial, retornando o nome
    do diretório sendo visitado(diretórios) e uma lista de seus arquivos(arquivos"""


# Programa 9.10 - Árvore de diretórios sendo percorrida
#import sys
#import os
#for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
 #   print("\nCaminho:", raiz)
  #  for d in diretorios:
   #     print(f"   {d}/")
    #for f in arquivos:
     #   print(f"   {f}/")
    #print(f"{len(diretorios)} diretório(s), {len(arquivos)} arquivo(s)")



import sys
import os
import os.path
# este módulo ajuda com a conversão de nomes de arquivos para links
# válidos em HTML
import urllib.request

mascara_do_estilo = "'margin: 5px 0px 5px %dpx;'"


def gera_estilo(nível):
    return mascara_do_estilo % (nível * 20)


def gera_listagem(página, diretório):
    nraiz = os.path.abspath(diretório).count(os.sep)
    for raiz, diretórios, arquivos in os.walk(diretório):
        nível = raiz.count(os.sep) - nraiz
        página.write(f"<p style={gera_estilo(nível)}>{raiz}</p>")
        estilo = gera_estilo(nível+1)
        for a in arquivos:
            caminho_completo = os.path.join(raiz, a)
            tamanho = os.path.getsize(caminho_completo)
            link = urllib.request.pathname2url(caminho_completo)
            página.write(f"<p style={estilo}><a href='{link}'>{a}</a>  ({tamanho} bytes)</p>")


if len(sys.argv) < 2:
    print("Digite o nome do diretório para coletar os arquivos!")
    sys.exit(1)

diretório = sys.argv[1]

página = open("arquivos.html", "w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
""")
página.write(f"Arquivos encontrados a partir do diretório: {diretório}")
gera_listagem(página, diretório)
página.write("""
</body>
</html>
""")
página.close()