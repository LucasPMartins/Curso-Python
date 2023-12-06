'''
Faça um programa que leia algo pelo teclado e 
mostre na tela o seu tipo primitivo e todas as 
informaçãoes possiveis sobre ela
'''

n = input('Digite algo:')
print(f'O tipo digitado é {type(n)}')
print(f'É alfanúmerico: {n.isalnum()}')
print(f'É númerico: {n.isnumeric()}')
print(f'É alfabético: {n.isalpha()}')
print(f'É decimal: {n.isdecimal()}')
print(f'É ASCII: {n.isascii()}')
print(f'É digit:{n.isdigit()}')
print(f'É válido{n.isidentifier()}')
print(f'É uma str com só letras minusculas: {n.islower()}')
print(f'É uma str com só letras maiusculas: {n.isupper()}')
print(f'É printavel: {n.isprintable}')
print(f'É um espaço: {n.isspace()}')
print(f'É um titulo: {n.istitle()}')