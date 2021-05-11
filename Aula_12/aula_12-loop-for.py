carros = ['HRV', "GOLF", "ARGO","FOCUS"]

for carro in carros:
    print(carro)

for n in range(len(carros)):
    print(n,"-", carros[n])

for carro in carros:
    print(carro)
    if(carro == "GOLF"):
        print("    GT")
print('---------------------------------')
for x in ['HRV', "GOLF", "ARGO","FOCUS"]:
    print(x)


# Utilizando o break
for n in range(10):
    carros.append(f"carro{n}")

print(carros)

for n in carros:
    if(n == 'carro1'):
        break
    print(n)
print("Fim do programa")