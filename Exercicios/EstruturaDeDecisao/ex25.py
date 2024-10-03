# 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

print("Responda as seguintes peguntas com SIM OU NÂO")

lista = ["Telefonou para a vítima?","Esteve no local do crime?",
        "Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]

count = 0
for pergunta in lista:
    while True:
        print(pergunta)
        resposta = input('R:').upper()
        if resposta == 'SIM':
            count += 1
            break
        if resposta == 'NÃO':
            break

if count > 1:
    if count == 2:
        print('Suspeito')
    elif count == 3 or count == 4:
        print('Cúmplice')
    else:
        print('Assassino')
else:
    print("Inocente")

