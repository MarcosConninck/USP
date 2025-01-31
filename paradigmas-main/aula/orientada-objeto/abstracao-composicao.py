from abc import ABC, abstractmethod


class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        raise NotImplementedError('Este método deve ser implementado')

    # ao implementar outro método, ele passa a ser obrigatório nos classes
    # que herdam da classe FormaGeometrica.
    # Isso se chama injeção de dependência

    # @abstractmethod
    # def calcular_perimetro(self):
    #     raise NotImplementedError('Perimetro deve ser implementado')


class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio

    # Obriga Circulo a ter este método definido
    def calcular_area(self):
        area = 3.14 * self.raio ** 2
        return area


class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.altura * self.largura
        return area


circulo1 = (Circulo(raio=10))
circulo2 = (Circulo(raio=20))

print(circulo1.calcular_area())  # 314.0
print(circulo2.calcular_area())  # 1256.0

retangulo1 = (Retangulo(10, 5))
print(retangulo1.calcular_area())  # 50


class Motor:

    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True
        print('Vrumm')


class Carro(Motor):

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f'Carro da marca: {self.marca}, e modelo: {self.modelo}')


carro1 = Carro('VW', 'gol')
carro1.exibir_detalhes()

motor1 = Motor(potencia=200)
motor1.ligar_motor()  # ligado = True

carro1.potencia = 100
print(carro1.potencia)
carro1.ligar_motor()
print(carro1.ligado)
