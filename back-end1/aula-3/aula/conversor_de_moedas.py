taxa_euro_real = 6.18
taxa_yene_real = 0.037


def verifica():
    def conversao(real):
        novo_valor_euro = round((real / taxa_euro_real), 2)
        novo_valor_yene = round((real / taxa_yene_real), 2)
        print(f'R${real} valem: {novo_valor_euro} euros')
        print(f'R${real} valem: {novo_valor_yene} yenes')
    try:
        real = float(input("digite o valor de reais que quer converter: "))
        return conversao(real)
    except (ValueError):
        print('Digite apenas números')


verifica()
