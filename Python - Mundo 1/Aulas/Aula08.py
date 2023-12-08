# import math

#print(f'A raiz de {num} é {math.ceil(raiz)}')

from math import sqrt,floor,ceil

num= int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {raiz}')

print(f'A raiz de {num} é {raiz:.2f}')

print(f'A raiz de {num} é {ceil(raiz)}')

print(f'A raiz de {num} é {floor(raiz)}')


import random
num = random.randint(1,10)
print(num)
