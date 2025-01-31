# recursão

# entrada -> função -> saida(propria função)

# numero = int(input('Qual o valor que você quer a fatorial?'))


def fatorial(numero):
    if numero == 0:
        return 1
    return numero * fatorial(numero-1)


# print(fatorial(numero))


# fibonacci
# 0 1 1 2 3 5 8 13 ...
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(8))
