#A confederação nacional de natação precisa de um programa que leia;
#O ano de nascimento de um atleta e mostre sua categoria de acordo com a idade!
#Até 9 anos:Mirim
#Até 14 anos:Infantil
#Até 19 anos:Junior
#Até 20 anos:Sênior
#Acima:Master

n1 = int(input('Digite o ano em que você nasceu exemplo 2009: '))

if n1 >= 2015:
    print(f'Você tem {2024-n1} anos, e está na categoria Mirim!')
elif n1 >= 2010:
    print(f'Você tem {2024-n1} anos, e está na categoria infantil!')
elif n1 >= 2005:
    print(f'Você tem {2024-n1} anos, e está na categoria junior!')
elif n1 >= 2004:
    print(f'Você tem {2024-n1} anos, e está na categoria Sênior!')
elif n1 <= 2003:
    print(f'Você tem {2024-n1} anos, e está na categoria Master!')