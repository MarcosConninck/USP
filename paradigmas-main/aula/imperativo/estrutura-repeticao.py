# Somar números até atingir um limite
inicial = 0
valor_a_somar = 1
limite = 100

while inicial < limite:
    inicial += valor_a_somar
    valor_a_somar += 1
    # print(inicial)

# Encontrar primeiro numero divisivel por 7 em um intervalo
lista = range(0, 101)

# for n in lista:
# if (n % 7 == 0):
# print(n)

# Verificar se todos os ítens de uma lista são positivos

lista1 = [1, 2, 3, 4, 5]
lista2 = [-1, -2, 0, 3, 5]


def verifica_positivo(lista_verificar):
    todos_positivos = True
    for x in lista_verificar:
        if x < 0:
            todos_positivos = False
            print('tem um número negativo na lista')
            break

    if todos_positivos:
        print('todos são positivos')


verifica_positivo(lista1)
verifica_positivo(lista2)
