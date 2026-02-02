entrar_ou_sair = input('Deseja entrar ou sair? (S/N) ')

while entrar_ou_sair == 'S':
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))

    operador = input('Digite um operador: ')

    if operador == '+' or 'somar':
        print(numero1 + numero2)
    elif operador == '-' or 'subtrair':
        print(numero1 - numero2)
    elif operador == '*' or 'multiplicar':
        print(numero1 * numero2)
    elif operador == '/' or 'dividir':
        print(numero1 / numero2)
    if operador == 'S':
        print('Você saiu do programa')
        break