nome = input('Digite seu nome completo: ')
nome = nome.upper()
print('Seu nome em letra maiuscula:{}'.format(nome))
nome = nome.lower()
print('Seu nome com letras minusculas:{}'.format(nome))
nome = len(nome.replace(" ",""))
print('Seu nome contém {} letras'.format(nome))

