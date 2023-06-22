import random
import time

nome = int(input('Tente adivinhar o número que estou pensando de 0 a 5: '))
print('Estou pensando...')
time.sleep(3)
num = random.randint(0,5)

if num == nome:
    print('Você acertou!')
else:
    print('Você errou! Tente mais uma vez')
 
    