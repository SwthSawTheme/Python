t1 = float(input('Digite o primeiro lado: '))
t2 = float(input('Digite o segundo lado: '))
t3 = float(input('Digite o terceiro lado: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os seguimentos acima forma um triangulo!')
else:
    print('Não formam um triangulo!')