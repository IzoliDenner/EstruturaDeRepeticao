#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Insira sua nota de 0 a 10:\n'))
while (nota > 10) or (nota < 0):
    nota = float(input('Valor Inválido !!! Tente novamente:\n'))
if (nota >= 0) or (nota <=10):
    print(f'Sua nota é: {nota}')


