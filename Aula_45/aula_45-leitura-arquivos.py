nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'r')

print(f.read())
f.close()
#----------------------------------------

nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'r')
print(f.read(10)) # leitura dos 10 primeiros caracteres desse aquivo

f.close()

#----------------------------------------
nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'r')
print(f.readline()) # lê linha a linha e posiciona o cursor no final de cada linha
print(f.readline()) # lê linha a linha e posiciona o cursor no final de cada linha

f.close()

#----------------------------------------
nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'r')
for linha in f:
    print(linha)

f.close()

#----------------------------------------
nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'r')
print(f.readlines()) #coloca cada linha em uma lista
f.close()

#----------------------------------------
nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'r')
for linha in f.readlines():
    print(linha) #cimprime cada termo da lista
f.close()

#----------------------------------------
# USANDO RE
import re
nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'r')

res = re.sub('\s','-',f.readline())
print(res) 
f.close()

nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'w')

f.write(res) # escreve o texto com espeços substituidos por traços
f.close()

