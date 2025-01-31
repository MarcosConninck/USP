from utils import calcula_media, verifica_aprovacao

notas_aluno = [7, 4, 5, 8, 9, 4]
mensagem = 'A média do aluno foi: '


print(mensagem, calcula_media(notas_aluno))
print(verifica_aprovacao(calcula_media(notas_aluno)))
