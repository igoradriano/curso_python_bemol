# FUNCAO SEM PARAMETRO
def divisor():
    print("---------------------------")
    print(" FIM!")

# FUNCAO COM PARÂMETRO
def somar(num1,num2):
    soma = n1 + n2
    print(f"A soma de {n1} e {n2} é igual a {soma}")

# FUNCAO COM RETORNO
def multiplicar(num1,num2):
    res = n1 * n2
    print(f"A multiplicação de {n1} e {n2} é igual a {res}")
    return res


# USANDO AS FUNCOES
n1 = 10
n2 = 20
somar(n1,n2)
divisor()
b = multiplicar(n1,n2)
print(b)