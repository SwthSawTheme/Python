n1 = int(input('Digite uma nota: '))
n2 = int(input('Digite a segunda nota:'))

res = (n1 + n2) / 2

if res >= 6:
    print('Passou de ano!')
else:
    print('Você reprovou!')