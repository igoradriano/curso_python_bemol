l_carros = ['HRV', "Golf", "Argo"]

t_carros = ("HRV", "Golf", "Argo")


# PRINT TUPLA
for x in t_carros:
    print(x)
try:
    t_carros[0] = 'Ferrari'
except TypeError as err:
    print(err, "Não podemos modificar tuplas")


# PRINT LISTA
for x in l_carros:
    print(x)

l_carros[0] = "Ferrari"
print(l_carros)

# FORMAS DE ALTERAR TUPLAS
print("Tupla antes: ",t_carros)
l_carros = list(t_carros)
l_carros[1] = "Lamborghini"
print("Lista intermediaria: ", l_carros)
t_carros = tuple(l_carros)
print("Tupla depois: ",t_carros)