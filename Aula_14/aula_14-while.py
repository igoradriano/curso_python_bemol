import os
os.system('cls')


i = 0
while i <9:
    print(i)
    i+=1 # condicao de parada

i = 0
# Usando o loop infinito
while True:
    i+=4    
    print(i)
    if i > 100:
        print("Valor final",i)
        break

i = 0
while i<10:
    print(i)
    i+=1
    if i>=5:
        break
print("Fim do loop")


carros = ['HRV', "GOLF","ARGO","ONIX","OCUS"]
i = 0
tam = len(carros)

while i < tam:
    print(carros[i])
    i +=1
print("\nFim do loop")


# While com input
carro = input("Digite o nome de novo carro: ")
while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome de novo carro:")


os.system('cls')
for x in carros:
    print(x)
print("\nFim do loop")
