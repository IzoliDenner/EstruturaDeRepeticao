# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Digite seu nome:'))
while (len (nome) <= 3):
    print('Seu nome precisa ter mais do que 3 caracteres.!!')
    nome = str(input('Digite seu nome:'))

idade = int(input('Digite sua idade:'))
while (idade < 0 or idade > 150):
    print('Sua idade deve estar entre 0 a 150:')
    idade = int(input('Digite sua idade:'))

salario = float(input('Digite seu salario: '))
while (salario < 0):
    print('Seu salario deve ser maior que "0":')
    salario = float('Digite seu salario: ')

sexo = str(input('Digite seu sexo:'))
while (sexo !='F' and sexo != 'M'):
    print('Para Sexo Masculino digite "M", para Feminino "F"')
    sexo = str(input('Digite seu sexo:'))

estado = str(input('Digite Seu estado Civil:'))
while (estado != 'S' and estado !='C' and estado !='V' and estado !='D'):
    print('Digite "S" Para Solteiro, "C" para Casado, "V" para Viuvo ou "D" para divorciado')
    estado = str(input('Digite Seu estado Civil:'))

print (f'{nome}, tem {idade} anos, recebe R${salario} de salario, se considera do Sexo: {sexo} e seu estado Civil é {estado}.')


