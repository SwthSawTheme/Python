salario = float(input('Digite o valor do salário do funcionario: '))

if salario >= 1250:
    aumento = 10
else:
    aumento = 15

aumento2 = (aumento / 100) * salario
aumento3 = aumento2 + salario

print(f'O funcionario tem um sálario mensal de R${salario:.2f} e teve {aumento}% de aumento, recebendo R${aumento2:.2f} a mais no salário!')
