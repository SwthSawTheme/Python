print('\n\nCalculo de média de alunos!\n')

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Reprovado!!')
elif 5.0 <= media <= 6.9:
    print('Recuperação!!')
else:
    print('Você passou!') 