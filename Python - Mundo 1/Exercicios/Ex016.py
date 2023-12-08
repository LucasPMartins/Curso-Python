'''
Crie um programa que liea um número Real 
qualquer pelo teclado e mostre na tela a sua porção inteira
'''
from math import trunc # Trunc parte inteira, floor arredonda pra baixo, ceil para cima 

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')

# ou

print(f'O número {num} tem a parte inteira {int(num)}')
