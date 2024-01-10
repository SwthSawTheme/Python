print('\n\nBem vindo a IA, vamos comparar dois números inteiros!')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'{num1} é maior que o número {num2}!')
elif num2 > num1:
    print(f'{num2} é maior que o número {num1}!')
elif num1 == num2:
    print('Ambos os números são iguais!')