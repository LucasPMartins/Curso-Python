'''
Escreva um programa que pergunte a quantidade de Km 
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço, sabendo que o
carro custa R$60 por dia e R$0,15 por Km rodado.
'''

d = int(input('Quantos dias o carro foi alugado?\nR:'))
r = float(input('Quantos Km rodados?\nR:'))
preço = d * 60 + 0.15 * r
print(f'O preço do aluguel do carro é R${preço:.2f}')


