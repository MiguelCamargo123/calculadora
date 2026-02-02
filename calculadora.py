numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

operador = input('Digite um operador: ')

if operador == '+' or 'somar':
    print(numero1 + numero2)
elif operador == '-' or 'subtrair':
    print(numero1 - numero2)
elif operador == '*' or 'multiplicar':
    print(numero1 * numero2)
elif operador == '/' or 'dividir':
    print(numero1 / numero2)