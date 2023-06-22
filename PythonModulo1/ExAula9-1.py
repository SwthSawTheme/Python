nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letra maiuscula:{}'.format(nome.upper()))
print('Seu nome com letras minusculas:{}'.format(nome.lower()))
print('Seu nome contém {} letras'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('Seu primeiro nome contém {} letras'.format(len(nome[0])))

