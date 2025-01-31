def calcula_media(lista_notas):
    total = 0
    qtd_provas = 0
    for nota in lista_notas:
        total += nota
        qtd_provas += 1

    media = total / qtd_provas
    return round(media, 2)


def verifica_aprovacao(media_notas):
    if media_notas < 7:
        return 'reprovado'
    return 'aprovado'
