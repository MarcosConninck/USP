# valor = 10
valores = [1, 2, 3, 4, 5]

# dobro = lambda x: x * 2
lista_dobrada = list(map(lambda x: x * 2, valores))

# print(dobro(valor))
# print(lista_dobrada)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_pares = map(lambda x: x % 2 == 0, numeros)

# print(soma_pares)

# total = 0
# for numero in numeros:
#     if numero % 2 == 0:
#         total += numero
# print(total) # 30

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)
