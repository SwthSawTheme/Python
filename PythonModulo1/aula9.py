#Manipulação de caracteres

frase = 'Curso em video python'

print(frase[9:21])
print(frase[:5])
print(frase [9::3])
print(frase.count('o',0,13))
print(len(frase))
print(frase.find('deo'))
print(frase.find('teste'))
print('python' in frase)

frase = frase.lower()
frase = frase.replace('python','teste')
#frase = frase.split()
#frase = '---'.join(frase)
print(frase)

print("""Teste de print com quebra
de linha  
      """)
teste = frase.split()
print(teste[0])

