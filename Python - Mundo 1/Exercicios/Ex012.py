''' 
Faça um algoritmo que leia o preço de um produto e 
mostre seu novo preço, com 5% de desconto.
'''

p = float(input('Digite o valor do produto:'))
desconto = (p*5)/100
print(f'O preço do produto (R${p}) com desconto de 5% é R${p-desconto:.2f}')