'''
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro =  Ana
último = Souza
'''

nome = input('Digite seu nome completo:').strip()

temp = nome.split()

print(f'primeiro: {temp[0]}')
print(f'último: {temp[len(temp)-1]}')