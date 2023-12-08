'''
O mesmo porfessor do desafio anterio quer sortear 
a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos alunos e mostre 
a ordem sorteada.
'''

from random import shuffle

aluno1 = input('Digite o nome do aluno 1:')
aluno2 = input('Digite o nome do aluno 2:')
aluno3 = input('Digite o nome do aluno 3:')
aluno4 = input('Digite o nome do aluno 4:')

lista = [aluno1,aluno2,aluno3,aluno4]

shuffle(lista)

print('\nA ordem sorteada é:\n')

print(lista)