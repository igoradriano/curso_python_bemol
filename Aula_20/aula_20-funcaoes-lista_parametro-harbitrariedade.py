
# FUNCAO COM 'n' ARGUMENTOS
def dividir(*n):
    res = n[0]
    for idx,numero in enumerate(n):
        print("parcial",res)
        if idx < len(n)-1:
            res = res/n[idx+1]
    for numero in n:
        print('Números Usados: ', numero)
    print(f'Resultado final: {res}')


dividir(100,2,2,2,2,2,2,2,2)


# FUNCAO COM VALOR DEFAULT
def carros(c = 'HONDA'):
    print("MODELO: ", c)


carros()
carros("Ford")


# FUNCAO UTILIZANDO LISTA COMO PARAMETRO

def somar(num):
    r = 0
    for n in num:
        r +=n
    print("Soma = " + str(r))

print('--------------------------------------')
lista = [1,2,3,4,5,6,7,8,9,10,11]
somar(lista)