''' 
Faça um programa que leia o comprimento do cateto oposto 
e do cateto adjacente de um triangulo retangulo, calcule e 
mostre o comprimento da hiponenusa.
'''
from math import sqrt,pow

co = float(input('Digite comprimento do cateto oposto:'))
ca = float(input('Digite comprimento do cateto adjacente:'))
h = sqrt(pow(ca,2)+pow(co,2))
# ou
# h = (co ** 2 + ca ** 2) ** (1/2)
# h = math.hypot(co,ca)
print(f'O comprimento da hiponenusa é {h:.2f}')