import re
import os
nome = 'teste2.txt'
caminho = 'C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_46/'

if os.path.exists(caminho + nome) : #verificando se existe o caminho
    os.remove( caminho + nome)
    print('Arquivo apagado')
else:
    f = open(caminho +nome,'w')
    f.write("Arquivo criado")
    f.close()
    print("Arquivo criado")