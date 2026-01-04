print('Bem vindo a calculadora de gorjetas!')
valor = float(input('Qual foi o valor da conta? R$ '))
gorjeta = int(input('Qual o valor da gorjeta: 10, 12 ou 15? '))
conta_div = int(input('Dividir a conta por quantas pessoas? '))

por_gor = (((gorjeta / 100) * valor) + valor) / conta_div
por_gor = round(por_gor, 2)

print(f'Cada pessoa deve pagar R$: {por_gor} reais')
