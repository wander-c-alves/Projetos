try:
    valor1 = int(input('Digite o Primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    if valor1 > valor2:
        print(f'O primeiro valor: {valor1} é maior que o segundo valor: {valor2}')
    elif valor2 > valor1:
        print(f'O segundo valor: {valor2} é maior que o primeiro valor: {valor1}')
    else:
        print('Valores iguais')

except ValueError:
    print('Você não digitou um valor valido')
