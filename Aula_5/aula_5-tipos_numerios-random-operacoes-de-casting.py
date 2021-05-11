num_i = 10
num_f = 5.2
num_c = 1j

x=num_i

try:
    print("Valor: " + x + "Tipo: " + type(x))
except TypeError as err:
    print(err,".Não conseguimos contatenar uma string e um tipo")
except NameError as err:
    print(err,".Não conseguimos contatenar uma string e um inteiro")
finally:
    print("Obrigado, Tchau!")


# Agora com uma operação de casting (str) consegiremos
print("Valor: " + str(x) + " Tipo: " + str(type(x)))

x=num_f
print("Valor: " + str(x) + " Tipo: " + str(type(x)))

x=num_c
print("Valor: " + str(x) + " Tipo: " + str(type(x)))

# Agora vamos utilizar outro casting

x = 1
y = 2.3
z = 1j

z = int(x)
w = float(x)


print("Valor: " + str(z) + " Tipo: " + str(type(z)))


print("Valor: " + str(w) + " Tipo: " + str(type(w)))


# Podemos trabalhar com numeros aleatorios de 1 a 100
import random
num_r = random.randrange(1,100)

x = num_r

print("Valor: " + str(num_r) + " Tipo: " + str(type(num_r)))


#podemos criar um array para armazenar 6 valores aleatorios de 0 a 100

numr=[
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
]

for n in numr:
    print("Valor: " + str(n))