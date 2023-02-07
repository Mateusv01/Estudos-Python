# Se a pessoa deve ou não pagar o iposto de acordo com a renda 


from operator import truediv
from xml.dom.expatbuilder import ElementInfo
from xmlrpc.client import FastParser


renda = 1000
imposto = 1200

print (renda >= 1200 and imposto >= 1200)

#=============================================#

a = 1
b = 2 

print(a > b and True)

#===============================================#

matéria1 = 7
matéria2 = 7
matéria3 = 7

média = float(matéria1 + matéria2 + matéria3) /3

aprovado = média >= 7

print (aprovado)
if aprovado == True:
    print("Hoje é seu aniversário esta de parabiens ")
elif aprovado == False:
    print("PARABÉNS ZE HAHAHHAHAHAHHA tá reprovado")

