# fatiamento

# frase = 'Curso em Vídeo Python'

# frase[9] = V
# frase[9:13] = Víde
# frase[:5] = Curso 
# frase[15:] = Python
# frase[9::3] = VePh

# Análise

# len(frase) = 21 #comprimento
# frase.count('o') = 3 #quantas vezes 'o' aparece na string(frase)
# frase.count('o',0,13) = 1 #quantas vezes 'o' aparece na string(frase) de 0 até 12
# frase.find('deo') = 11 #encontra a posição inicial de 'deo' na string
# frase.find('Android') = -1 # 'Android' não existe em frase
# 'Curso' in frase = T # Exsite 'Curso' em frase? se sim T, se não F

# Transformação

# frase.replace('Python','Android')
# frase.upper() = 'CURSO EM VÍDEO PYTHON'
# frase.lower() = 'curso em vídeo python'
# frase.capitalize() = 'Curso em vídeo python'
# frase.title() = 'Curso Em Vídeo Python'

# frase = '   Aprenda Python  '
# frase.strip() = 'Aprenda Python'
# frase.rstrip() = '   Aprenda Python'
# frase.lstrip() = 'Aprenda Python  '

# Divisão

# frase.split() = ['Curso','em','Vídeo','Python']

# Junção

# ' '.join(frase) = 'Curso em Vídeo Python'

frase = 'Curso em Vídeo Python'

print(frase[3:13])

print("""adkasldjasojdoajsdasdada
djasdjasdadad
      ja
      sjdajda
      da
      dj """)

print(frase.count('o'))

print(frase.upper().count('O'))



