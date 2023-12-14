'''
Crie um programa que leia o nome de uma 
pessoa e diga se ela tem 'Silva' no nome
'''

nome = input('Digite seu nome completo:').strip()


r = nome.upper().find('SILVA')

if r == -1:
    print('Seu nome não contém a palavra "Silva"')
else:
    print('Seu nome contém a palavra "Silva"')

'''
'SILVA' in nome.upper()
'''