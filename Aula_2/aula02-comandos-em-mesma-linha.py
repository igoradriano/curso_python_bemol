num = 1
num = 's'
num = True
print("num = ", num)
canal = "CFB Cursos"
curso = "Curso dePython"
print(canal,curso)

#Para colocar mais de um comando na mesma linha:
num1=1; num2=2; num3=3; 
total = num1 + num2 + num3
print("total =" ,total)

#comentario de multtiplas linhas:
''' Posso escrever
apertar enter
enter
enter
enter
'''
# Comentario de uma linha
try:
    print( canal + "-" + curso)

    if 10 > 2:
        print("Devemos indentar")
    else:
        print("Irá dar errado")
    print("FIM")
except:
    print("Deu erro")

finally:
    print("depois de executar o try ou o except executa isso aqui ")
