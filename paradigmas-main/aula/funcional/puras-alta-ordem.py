# Função pura
def soma(a, b):
    return a + b


# print(soma(2, 3))

# Função de alta ordem -> recebe como input uma outra função


def aplicar_duas_vezes(func, valor):
    return func(func(valor))


def incrementar(x):
    return x + 1


def elevar_ao_quadrado(x):
    return x ** 2


def dividir_por_2(x):
    return x / 2


# print(aplicar_duas_vezes(elevar_ao_quadrado, 6))

numeros = [1, 2, 3, 4, 5, 6]


def aplicar_transformacao(funcao, lista):
    return [funcao(x) for x in lista]


numeros_quadrado = aplicar_transformacao(elevar_ao_quadrado, numeros)
numeros_quadrado_dividido_por_dois = aplicar_transformacao(dividir_por_2, numeros_quadrado)
print(numeros_quadrado)
print(numeros_quadrado_dividido_por_dois)
