# Crie um programa que leia nome e duas notas e guarde tudo em uma lista composta. No final mostrem um boletim
# contendo a média de cada um e permita que o usuário mostre as notas  de cada aluno individualmente.

fichas = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input("Nota1: "))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    fichas.append([nome, [nota1, nota2], media])
    pergunta = str(input("Quer continuar? [S/N]")).upper()
    if pergunta == 'N':
        break
print('_=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Notas":<10}{"Média":>8}')
print('-' * 26)
for i, (nome, notas, media) in enumerate(fichas):
    notas = ' '.join(str(x) for x in notas)
    print(f'{i + 1:<4}{nome:<10}{notas:<10}{media:>8.1f}')
