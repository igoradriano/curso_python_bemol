aula = True
print(aula)

a = 10 < 15
print(a)

a = 10 > 15
print(a)

aula = "Matematica"
print(aula)
#Convertendo para booleano com casting

# Imprime verdadeiro pois eu tenho o conteudo dentro da variavel
print(bool(aula))

#vai dar false, pois nao tem conteudo na variavel
aula = ''
print(bool(aula))

if aula:
    print("Possui texto")
else:
    print("Vazio")

# ex2:
aula = ''
print(bool(aula))

if aula == True:
    print(aula)
else:
    aula = 'True'
    print("Agora ela armazena uma string com o nome",aula)

    