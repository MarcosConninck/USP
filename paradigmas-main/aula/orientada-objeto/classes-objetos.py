# criando uma classe:

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}')

    def andar(self):
        print(f'{self.modelo} está andando, vruuuummmm')

    def parar(self):
        print(f'{self.modelo} parando..')


carro1 = Carro('VW', 'gol', '2006')
carro1.__str__()
carro1.andar()
carro1.parar()
