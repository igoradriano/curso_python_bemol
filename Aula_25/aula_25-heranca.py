class NPC():  #Super classe, classe pai
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    
    def info(self):
        print(f'Nome....: {self.nome}')
        print(f'Time....: {self.time}')
        print(f'Forca...: {self.forca}')
        print(f'Municao.: {self.municao}')
        print(f'Vivo....: {"sim" if self.vivo else "não"}')
        print(f'Energia.: {self.energia} ')
        print("---------------------------------------")

# Construiremos classes filhas agora:

class Soldado(NPC):
    def __init__(self, nome, time): # esse construtor vai sobrecrever o construtor da classe pai
        self.forca = 2000
        self.municao = 2000
        if self.forca <= 0:
            self.forca = 0
            self.vivo = False
        super().__init__(nome, time, self.forca, self.municao)

    def tiro(self, inimigo):
        dano = 10
        inimigo.forca = inimigo.forca - dano*40
        self.municao = self.municao - 80
        if self.municao <= 0:
            self.municao = 0
            dano = 0
        if inimigo.forca <= 0:
            inimigo.forca = 0
            inimigo.vivo = False



class Guarda(NPC):
    def __init__(self,nome, time):
        self.forca = 100
        self.municao = 20
        if self.forca <= 0:
            self.forca = 0
            self.vivo = False
        super().__init__(nome, time, self.forca, self.municao)
    
    def tiro(self, inimigo):
        dano = 50
        inimigo.forca = inimigo.forca - dano*15
        self.municao = self.municao - 30
        if self.municao <= 0:
            self.municao = 0
            dano = 0
        if inimigo.forca <= 0:
            inimigo.forca = 0
            inimigo.vivo = False



class Elite(NPC):
    def __init__(self,nome, time):
        self.forca = 700
        self.municao = 5
        super().__init__(nome, time, self.forca, self.municao)

    def inf(self):  # posso criar um novo método que chame o método da classe pai
        super().info()  # ou simplesmente posso chamar diretamente o método info da classe pai
        print("Método Exclusivo de Chamado do Elite")

    def tiro(self, inimigo):
        dano = 300
        inimigo.forca = inimigo.forca - dano
        self.municao = self.municao - 1
        if self.municao <= 0:
            self.municao = 0
            dano = 0
        if inimigo.forca <= 0:
            inimigo.forca = 0
            inimigo.vivo = False


s1 = Guarda('Olho Vivo', 'Time 1')
s2 = Soldado('Bala na Agulha', 'Time 1')
s3 = Elite('Ninja', 'Time 1')
s4 = Guarda('Tiro Certo', 'Time 2')
s5 = Soldado('Silencioso', 'Time 2')
s6 = Elite('Super Atento', 'Time 2')


s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()
s6.inf()

print("------------------------------------------------------------------")
s6.tiro(s3)
s6.tiro(s3)
s6.tiro(s1)
s6.tiro(s2)
s6.tiro(s4)
s6.tiro(s5)


s3.info()
s2.info()
s1.info()
s6.inf()
s1.tiro(s3)
s2.tiro(s3)
s2.tiro(s3)
s2.tiro(s3)
s2.info()



