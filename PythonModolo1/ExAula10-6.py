n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número:'))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print(f'O número maior é {maior}')
print(f'O número menor é {menor}')