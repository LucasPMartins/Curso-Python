'''
Crie um programa que leia o nome de uma cidade 
e diga se ela começa ou não com o nome "SANTO"
'''

cidade = input('Digite o nome da cidade:').strip()

print('A cidade começa com "Santo"?\nR:',end='')
aux = cidade.upper().split()
r = 'SANTO' in aux[0]
print(r)


'''
cidade[:5].upper() == 'SANTO'
'''
