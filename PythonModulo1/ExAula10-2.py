carro = int(input('Digite a velocidade do carro em Km: '))
multa = 7
if carro > 80:
    carro = carro - 80
    multa = carro * multa
    print(f'Você ultrapassou {carro}Km do permitido, e foi multado em R${multa:.2f}!')
else:
    print('Você está dentro do limite de velocidade!')
    