carros = ['HRV',"GOLF","ARGO","FOCUS","Ferrari","PRIUS"]

print(carros[0])
print(carros[-1])
print(carros[-2])

carros[3] = "FUSION"
print(carros)
print("Alteramos uma posicao da lista")

# Método Append

carros.append("FIT")
carros.append("Polo")
carros.append("Lamborghini")
print(carros)

# Método len

print(str(len(carros)) + " carros na lista")


#Método Remove
carros.remove("Lamborghini")
print(str(len(carros)) + " carros na lista")
print(carros)


# MÉTODO POP - remove o ultimo elemento da lista
carros.pop()
print(carros)

# MÉTODO DEL 
del carros[2]
print(carros)

# MÉTODO CLEAR -> Limpar lista inteira
carros.clear()
print(carros)

# COPIANDO LISTAS MÈTODO LIST()
carros = ['HRV',"GOLF","ARGO","FOCUS","Ferrari","PRIUS"]
carros2 = list(carros)
print(carros)


#FUNDIR 2 LISTAS
carros2 = ['FUSCA', "147", "Brasília", "Celta"]

carros3 = carros+carros2
print(carros3)
print(str(len(carros3)) + ' carros na lista')

