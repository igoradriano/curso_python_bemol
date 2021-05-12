nome = 'teste.txt'
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'wt')

# r - read - Leitura
# a - append - anexar
# w - write - Escrita
# x - create - criar
# t - texto (padrao)
# b - binario
txt = input("Digite um texto: ")
f.write(txt + "\n") # apaga tudo e escreve só o ultimo
f.close()

#----------------------------------------
f = open('C:/Users/Asus/Documents/GitHub/curso_python_bemol/Aula_44/' +nome,'a')
txt = input("Digite mais alguma coisa: ")
f.write(txt) # apaga tudo e escreve só o ultimo
f.close()

#---------------------------------------