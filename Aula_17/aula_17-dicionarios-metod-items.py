# Chave /valor -> Key/Value
carro = {
    'Fabricante':'Honda',
    'Modelo':'HRV',
    'Ano':'2016',
    'Cor':'Prata'
}

print(carro)
print(carro['Modelo'])
fab = carro['Fabricante']
print(fab)

# Método GET
ano = carro.get('Ano')
print(ano)


# Mudando Valores
carro['Cor'] = 'Preto'
print(carro)


# Imprimir chave
for key in carro:
    print(key)

# Imprimir Valor
for key in carro:
    print(carro[key])

# Imprimir Chave e Valor (.items)
for c,v in carro.items():
    print(c + ":" + v)

# Verificando se chave existe
if 'Modelo' in carro:
    print('Sim, Modelo é uma chave')

# Verificando o tamanho :

print("Tamanho do dicionario: " + str(len(carro))+ ' chaves')

# Criando uma nova chave
carro['Cambio'] = 'Automático'
print(carro)

# Remover chave de dicionario (POP)
carro.pop('Cambio')
print(carro)

# Remover chave de dicionario (DEL)
del carro['Fabricante']
print(carro)

# Limpar todos os elementos(CLEAR)
carro.clear()
print(carro)


# DICIONARIO DE DICIONARIOS
carros = {
    'Carro1':{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    'Carro2':{
        "Fabricante":"Fiat",
        "Modelo":"Uno"
    },
    'Carro3':{
        "Fabricante":"Ford",
        "Modelo":"Fiesta"
    }
}

print("-------------------------")
print(carros)
print("-------------------------")
print(carros['Carro1'])
print(carros['Carro1']['Fabricante'])


# Podemos tambem fazer assim:

Carro1 = {
    'Fabricante':'Honda',
    'Modelo':'HRV'
}

Carro2 = {
    'Fabricante':'Fiat',
    'Modelo':'Uno'
}

Carro3 = {
    'Fabricante':'Ford',
    'Modelo':'Fiesta'
}

carroes = {
    'C1':Carro1,
    'C2':Carro2,
    'C3':Carro3
}
print('-----------------------------')
print(carroes)
print(carroes['C1']['Fabricante'])