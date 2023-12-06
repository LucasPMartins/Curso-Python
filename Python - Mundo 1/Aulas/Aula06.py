#================== TEORIA ==================
'''
# Tipos Primitivos e Saída de Dados

n1 = input('Digite um número:') # n1 recebe uma string
n2 = input('Digite mais um número:')
s = n1 + n2
print('A soma vale',s)

# Forma correta

n1 = int(input('Digite um número:')) # transforma a string em um inteiro
n2 = int(input('Digite mais um número:'))
s = n1 + n2
print('A soma vale',s)

#Tipos primitivos

int 7 -4 0 9875
float 4.5 0.076 -15.223 7.0
bool true false ou T F
str 'olá' '7.5' ''

print('A soma vale',s)
#ou
print('A soma vale {}'.format(s))
'''
#================== PRATICA ==================

n1 = input('Digite um número:')
print(type(n1))

n1 = int(input('Digite um número:')) # transforma a string em um inteiro
n2 = int(input('Digite mais um número:'))
s = n1 + n2
# print ('A soma entre',n1,'e',n2,'vale',s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s)) # Meio antigo
print(f'A soma entre {n1} e {n2} é {s}') # Modo mais moderno

n = input('Digite algo:')
print(n.isnumeric())
n = input('Digite algo:')
print(n.isalpha())
n = input('Digite algo:')
print(n.isalnum())