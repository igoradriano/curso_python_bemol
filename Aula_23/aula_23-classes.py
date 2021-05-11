class Pessoa:
    nome = ''
    sobrenome = ''
    cpf = ''

class Carro:
    vel_max = 0
    ligado = False
    cor = ''
    def __init__(self,marca,modelo,ano,potencia,n_portas):  # parametros obrigatorios na hora da criacao
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.potencia = potencia
        self.n_portas = n_portas

p1 = Pessoa()
c1 = Carro('Honda','Civic',2012, 700,2)


# Modificando atributos do objeto p1 de classe Pessoa
p1.nome = 'Igor'
p1.sobrenome = 'Rodrigues'
p1.cpf = 98712284220

# Modficando objetos c1 da classe Carro
c1.marca = 'Ferrari'
c1.modelo = 'Enzo'
c1.ligado = True

# Printando 
print(p1.nome, ' - ',p1.cpf)
print(c1.marca, ' ',c1.modelo)

estado = 'sim' if c1.ligado == True else 'não'
print("Ligado: ", estado)

