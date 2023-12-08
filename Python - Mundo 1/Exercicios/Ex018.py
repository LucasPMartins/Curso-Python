'''
Faça um programa que leia um ângulo qualquer 
e mostre na tela o valor do seno, cosseno e tangente desse angulo.
'''

from math import cos, sin, tan, radians
# cos,sin,tan realizam operações com valores em radianos

a = float(input('Digite um ângulo qualquer em graus: '))
a_rad = radians(a)  # Converte graus para radianos
print(f'O seno de {a}° é {sin(a_rad):.2f}')
print(f'O cosseno de {a}° é {cos(a_rad):.2f}')
print(f'A tangente de {a}° é {tan(a_rad):.2f}')
