# Formas de iniciar uma lista
carros = []
carros = list()
carros = ['HRV', 'Civic', "WRV", "CRV", "CITY"] # Array/list


carros[2] = "Fusion"
print("Subistituimos um carros, colocamos o ", carros[2])

for carro in carros:
    print(carro)

# VETOR - lista de listas
locadora = [['HRV',2019,'Honda',400],['UNO',2020,'Fiat',80],['California',2021,'Ferrari',400],['Veyron',2012,'Bugatti',1080]]

print(locadora[0][1])

print('---------------------------------')
print("Carros: ")
for carros in locadora:
    print(carros[0])

for itens in locadora:
    print(f"Marca: {itens[2]} - Modelo: {itens[0]} - Ano: {itens[1]} - Potencia: {itens[3]}cv")
    
for l,c1,c2,c3 in locadora:
    print("Linha: " + str(l) +"| Coluna: " + str(c1) + str(c2) + str(c3))

# INSERINDO DADOS
locadora.append(['KWID',2021,'Renalt',78])
locadora.append(['KWID',2021,'Renalt',78])
locadora.append(['KWID',2021,'Renalt',78])
locadora.append(['KWID',2021,'Renalt',78])
print(locadora)