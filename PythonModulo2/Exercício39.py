print('\n\nServiço Militar Obrigatório: Alistamento, Seleção Geral:\n')

nome = str(input('Digite seu nome: '))
data = int(input('Digite o ano em que você nasceu: '))

idade = 2023 - data

if data == 2006 or data == 2005:
    print(f'{nome} você tem {idade} anos e já pode se alistar ao exercito!')
elif data < 2006:
    print(f'{nome} você tem {idade} anos e passou {idade - 18} anos do alistamento militar obrigatório!')
elif data > 2006:
    print(f'{nome} você tem {idade} anos e falta {18 - idade} anos para o alistamento militar obrigatório!')
elif data > 2023:
    print('Digite uma data valida!')
    

