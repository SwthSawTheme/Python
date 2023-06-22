viagem = int(input('Digite a distancia da sua viagem em Kms: '))
d1 = 0.50
d2 = 0.45
if viagem <= 200:
    res = d1 * viagem
    print(f'Você pagou R${d1} centavos por Km, e o valor total ficou R${res:.2f}')
else:
    res1 = d2 * viagem
    print(f'Você pagou R${d2} centavos por Km, e o valor total ficou R${res1:.2f}')
    