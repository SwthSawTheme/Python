# Escreva um programa que leia um número inteiro qualquer, e peça para o usuário
# escolher qual será a base de conversão;

n1 = int(input('Digite um número inteiro que deseja converter: '))
n2 = int(input('Escolha a base a ser convertida: [1]Binaria [2]Octal [3]Hexadecimal: '))

if n2 == 1:
    binario = bin(n1)[1:]
    print(f'O número {n1} é {binario} em binario!')
elif n2 == 2:
    octal = oct(n1)
    print(f'O número {n1} é {octal} em octal!')
elif n2 == 3:
    hexadecimal = hex(n1)
    print(f'O número {n1} é {hexadecimal} em hexadecimal!')
else:
    print('Digite um número valido!')