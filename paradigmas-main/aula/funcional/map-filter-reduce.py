from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map -> itera cada elemento e aplica a função
# filter -> a partir de uma condição, dá um resultado
# reduce -> reduzir a um valor

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))

print(f'Números pares com filter: {numeros_pares}')
# retorna o objeto, por isso usar list()
print(f'Números impares com filter: {numeros_impares}')

numeros_dobrados = list(map(lambda x: x * 2, numeros))

print(f'Números dobrados com map: {numeros_dobrados}')

numeros_pares_dobrados = list(map(lambda x: x * 2, numeros_pares))

print(f'Números pares dobrados com map: {numeros_pares_dobrados}')

soma_numeros_pares_dobrados = reduce(lambda x, y: x + y, numeros_pares_dobrados)

print(soma_numeros_pares_dobrados)
