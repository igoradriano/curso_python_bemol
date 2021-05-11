# Neste caso não temos o except definido
try:
    print(x)
except :
    print("Erro, Você não criou a variável 'x'")

finally:
    print("Fim do Programa!")

#-------------------------------------------------------
# Neste caso temos o except definico
x = -10
try:
    print(x)
except NameError as err:
    print(err,"- Erro, Você não criou a variável 'x'")
else:
    print("Tudo certinho")
finally:
    print("Fim do Programa!")

#-------------------------------------------------------------
# Lançando uma exceção
num = "Bruno"
if not type(num) is int:
    raise Exception("Valor deve ser do tipo inteiro")
else:
    print(num)