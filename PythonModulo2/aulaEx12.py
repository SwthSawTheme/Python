import time

print('\n\nBem vindo ao bancocn, o banco onde proporcionar\ndívidas a nossos clientes, é a nossa maior alegria!\n')
print('Sou a assístente bancaria Gabrielli. Qual o seu nome?\n')

nome = str(input('Digite seu nome: '))
print(f'\nPrazer {nome}!É uma satisfação atende-lo!\n')
renda = float(input('Qual sua renda mensal liquída?: '))
print(f'\nÒtimo {nome}!')
casa = float(input('Qual o valor da casa que deseja comprar?: '))
print(f'\nMuito bem! Estamos quase acabando {nome} :D\n')
anos = int(input('Em quantos anos você deseja financiar?: '))

porcentagem = renda * (30/100)

parcela = anos * 12

valor = casa / parcela

if porcentagem < valor:
    print(f'{nome} o valor da parcela excede os 30% do seu salário!\nSeu financiamento não foi aprovado! Sinto muito :(')
    print(f'\nSegue abaixo os detalhes do contrato;\nSua renda mensal é de {renda:.2f}R$\nO valor da casa é de {casa:.2f}R$\nO número de parcelas é de {parcela} meses!\nO valor da parcela ficou em {valor:.2f}R$ a pagar!')
else:
    print(f'Você conseguiu aprovação para seu financiamento {nome}, estou muito feliz!\n!Embreve entraremos em contato para resolução contratual!')
    print(f'\nSegue abaixo os detalhes do contrato;\nSua renda mensal é de {renda:.2f}R$\nO valor da casa é de {casa:.2f}R$\nO número de parcelas é de {parcela} meses!\nO valor da parcela ficou em {valor:.2f}R$ a pagar!')
    
input('\n\n\nPressione enter para sair...')
print('Até mais!!')
time.sleep(5)

