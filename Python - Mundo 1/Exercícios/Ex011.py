''' 
Faça um programa que leia a largura e a 
altura de uma parede em metros, calcule a sua 
área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2m^2
'''

l = int(input('Digite a largura da parede em metros:'))
a = int(input('Digite a altura da parede em metros:'))

print(f'Para pintar uma parede {l}x{a} de área igual a {l*a},')
print(f'será necessário {(l*a)//2} litros de tinta')

