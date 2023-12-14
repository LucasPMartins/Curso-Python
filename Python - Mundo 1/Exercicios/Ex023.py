'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:
Digite um número:1834
unidade:4
dezena:3
centena:8
milhar:1
'''

num = int(input('Digite um número entre 0 e 9999:'))

print(f'unidade:{num % 10}')
print(f'dezena:{(num//10)%10}')
print(f'centena:{(num//100)%10}')
print(f'milhar:{(num//1000)%10}')


