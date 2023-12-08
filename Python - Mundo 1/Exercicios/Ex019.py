'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random

aluno1 = input('Digite o nome do aluno 1:')
aluno2 = input('Digite o nome do aluno 2:')
aluno3 = input('Digite o nome do aluno 3:')
aluno4 = input('Digite o nome do aluno 4:')

n = random.randint(1,4)

if n == 1:
    print(f'O aluno escolhido é {aluno1}')
if n == 2:
    print(f'O aluno escolhido é {aluno2}')
if n == 3:
    print(f'O aluno escolhido é {aluno3}')
if n == 4:
    print(f'O aluno escolhido é {aluno4}')


'''
OU
lista = [aluno1,aluno3,aluno2,aluno4]
escolha = random.choice(lista)
print(f'O aluno escolhido é {escolha}')
'''