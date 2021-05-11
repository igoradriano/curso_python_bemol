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
    
    def mostrar(self):
        print('Velocidade Máxima: ' +  str(self.vel_max) +" km/h")
        print('Cor..............: ' +  str(self.cor))
        print('Ligado...........: ' +  str(self.ligado))
        print('-----------------------------------------')

    def velocidade(self,v0, aceleracao, tempo):
        self.vel_max = (v0 + aceleracao*tempo)*3.6 - (aceleracao*0.987**2)*3.6



c1 = Carro('Honda','Civic',2012, 700,2)
# Modficando objetos c1 da classe Carro
c1.marca = 'Ferrari'
c1.modelo = 'Enzo'
c1.ligado = True

# Printando 
print(c1.marca, ' ',c1.modelo)
estado = 'sim' if c1.ligado == True else 'não'
print("Ligado: ", estado)


# Chamando métodos internos
c1.cor = 'Vermelho'
c1.velocidade(0,1.5,77)
c1.mostrar()