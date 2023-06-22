frase = str(input('Digite uma frase: ')).upper()
print('A letra A apareceu {} vezes!'.format(frase.count("A")))

print('A primeira letra A apareceu na posição {}'.format(frase.find("A")))

print('A ultima letra A apareceu na posição {}'.format(frase.rfind("A")))
