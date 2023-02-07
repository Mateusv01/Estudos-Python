""" Agora que sabemos alterar arquivos, vamos aprender como listá-los, manipular
    Diretórios, verificar o tamanho e data de criação"""

import os
os.getcwd()

"""
Podemos trocar de diretório em Python, mas antes precisamos criar diretórios para teste

CRIANDO PASTAS A,B,C 
mkdir a
mkdir b
mkdir c

"""

"""
Agora vejamos como trocar de diretório

"""

#os.chdir("a")
#print(os.getcwd())

#os.chdir("..")
#print(os.getcwd())


""" A função makedirs cria imediatamente diretórios intermediários"""

#os.makedirs("avô/pai/filho")
#os.makedirs("avô/mãe/filha")


#os.mkdir("velho")
#os.rename("velho","novo")

#os.rename("avô/pai/filho","avô/mãe/filho")


""" Para apagar um diretório use rmdir. Se quisesr apagar um arquivo use remove"""

#os.rmdir("a")

#os.remove("...txt")

""" Podemos solicitar uma listagem de todos os arquivos e diretórios usando a função listdir"""

#print(os.listdir("."))
#print(os.listdir("avô"))
#print(os.listdir("avô/pai"))


""" Em que (".") significa o diretório atual. A lista contém apenas o nome de cada arqivo


    O módulo os.path traz novas funções que vamsos usar aa obter informações sobre os arquivos
    As duas primeiras são: isdir e isfile, que retornam true se o nome passado for um diretório
    ou um arquivo respectivamente """

import os.path
for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a}")
    elif os.path.isfile(a):
        print(a)

""" Podemos verificar um arquivo que já existe com a função exists"""

if os.path.exists("z"):
    print("O diretório z existe")
else:
    print("O diretório z não existe")


""" Temos outras função que retornam mais informações sobre arquivos e diretórios
    como seu tamanho e data de modificação, criação e acesso"""


import time
import sys

nome = sys.argv[0]
print(f"Nome: {nome}")
print(f"Tamanho: {os.path.getsize(nome)}")
print(f"Criado: {time.ctime(os.path.getctime(nome))}")
print(f"Modificado: {time.ctime(os.path.getmtime(nome))}")
print(f"Acessado: {time.ctime(os.path.getatime(nome))}")