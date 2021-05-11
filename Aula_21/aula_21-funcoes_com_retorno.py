# FUNCAO UTILIZANDO LISTA COMO PARAMETRO

def somar(num):
    r = 0
    for n in num:
        r +=n
    print("Soma = " + str(r))
    return r

print('--------------------------------------')
lista = [1,2,3,4,5,6,7,8,9,10,11]
resultado = somar(lista) + 100

print(resultado)