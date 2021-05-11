x = 1
x2 = "CFB Cursos" # string
x3 = 15.6 #float
x4 = False #bool
n1=5;n2=2; x5 = complex(n1,n2) #num complexo (n1 - real, n2 - imag)

print(f"Valor: {x}")
print(f"Tipo: {type(x)}")

print(f"Valor: {x2}")
print(f"Tipo: {type(x2)}")

print(f"Valor: {x3}")
print(f"Tipo: {type(x3)}")

print(f"Valor: {x4}")
print(f"Tipo: {type(x4)}")

print(f"Valor: {x5}")
print(f"Tipo: {type(x5)}")


#Usando cast para mudar o tipo int para str para poder concatenar
print(f"Valor:" + str(x))
print(f"Tipo: " + str(type(x)))


#coleções:

# Array -> list
lista = ["carro", "aviao", "navio",1,2,3]  #array/list
print("Valor" + lista[0])
print("Tipo: " + str(type(lista)))
lista[4] = "Novo valor"
print(lista)
listarange = range(0,100,2)
print(listarange)
for n in listarange:
    print(n)



#Tuplas
tupla = ("array","lista","dicionario",1,2,3)
print(tupla)
try:
    tupla[0]="novo valor"
except:
    print("Não podemos alterar uma tupla depois de criada ")
finally:
    print("Obrigado, tchau")

for n in tupla:
    print(n)


# Dicionario

dicionario = {
    "canal":"CFB Cursos",
    "curso":"Curso e Python",
    "nome":"Bruno"
}

print("Valor: " + dicionario["nome"])
print("Tipo: " + str(type(dicionario)))

# SET - > nao repete valores
Set = {1,2,3,4,5,67,8}# set
print("Valor: " +str(Set))
print("Tipo: " + str(type(Set)))
print("Sete não repete valores")


frouzingSet = frozenset({1,2,3,4,5,6,7,8,9})
print("Valor: " +str(frouzingSet))
print("Tipo: " + str(type(frouzingSet)))
print(" Frozingset nao pode ser alterado e nao se repete")