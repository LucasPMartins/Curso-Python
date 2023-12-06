#Crie um programa que leia dois números e mostre a soma entre elas

n1 = int(input('Digite um número:')) # transforma a string em um inteiro
n2 = int(input('Digite mais um número:'))
s = n1 + n2
# print ('A soma entre',n1,'e',n2,'vale',s)
# print('A soma entre {} e {} vale {}'.format(n1,n2,s))  Meio antigo
print(f'A soma entre {n1} e {n2} é {s}')