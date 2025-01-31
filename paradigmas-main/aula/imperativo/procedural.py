numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in numeros:
    if i % 2 == 0:
        soma += i

print(soma)

# ou

soma_pares = sum(filter(lambda x: x % 2 == 0, numeros))

print(soma_pares)
