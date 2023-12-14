'''
Crie um programa que leia o nome completo de uma éssoa e mostre:
o nome com todas as letras maiusculas
o nome com todas minusculas
quantas letras ao todo( sem considerar espacos)
quantas letras tem o primeiro nome
'''

nome = input('Digite seu nome completo:').strip()

print('Seu nome com todas as letras maiúsculas: ',end='')
print(nome.upper())

print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')


aux = nome.split()
c = len(aux[0]) 

print(f'O primeiro nome ({aux[0]}) tem {c} letras')

aux = ''.join(aux)
c = len(aux)

print(f'O seu nome completo tem {c} letras')

'''
len(nome) - nome.count(' ') tamanho do nome sem todos os espaços
'''


