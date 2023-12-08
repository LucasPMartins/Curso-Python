'''
Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário com 15% de aumento
'''

p = float(input('Digite o salário do funcionário:'))
aumento = (p*15)/100
print(f'O salário do funcionário (R${p}) com aumento de 15% é R${p+aumento:.2f}')