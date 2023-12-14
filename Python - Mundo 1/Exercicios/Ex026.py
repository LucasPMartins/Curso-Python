'''
Faça um programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra "A"
em que posição ela aparece a primeira vez
em que posição ela aparece a ultima vez
'''

frase = input('Digite uma frase qualquer:').strip()

r = frase.upper().count('A')

if r != 0:
    print(f'A letra "A" aparece na frase {frase}, {r} vezes')
    print(f'A letra "A" aparece pela primeira vez na posição {frase.upper().find("A")+1}')
    i = 0
    contador = 0
    while i != r:
        if frase[contador].upper() == 'A':
            i += 1
        contador += 1
    print(f'A letra "A" aparece pela última vez na posição {contador}')
else: 
    print('A letra "A" não está presente na frase')

'''
frase.rfind('A')+1 # Procura pelo lado direito
'''



