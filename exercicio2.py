#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input('Digite seu nome de usuario: \n'))
senha = str(input('Digite sua senha: \n'))

while (usuario == senha):
    usuario = input('Usuário ou senha errado! Tente novamente. \nUsuário:\n')
    senha = input('Senha: \n')

else:
    print('Login efetuado com sucesso.')