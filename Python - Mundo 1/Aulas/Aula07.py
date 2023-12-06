# Operadores Aritméticos

# + soma
# - subtração
# * multiplicação
# / divisão
# ** potenciação
# // divisão interia
# % Resto da Divisão

# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2
# 5 % 2 == 1

#Ordem de Precedência

#1()
#2**
#3*,/,//,%
#4+,-

'oi' + 'olá'
'oi'*5
'='*20
print('='*20)

nome = input('Qual é o seu nome:')
print(f'prazer em te conhecer {nome:=^20}!',end=' ')
print(f'prazer em te conhecer {nome:>20}!')
print(f'prazer \n em te \n conhecer {nome:<20}!')
print(f'prazer em te conhecer {nome:=>20}!', end = ' >>> ')

s = 3.44444555555555
print(f'Divisão é {s:.3f}')