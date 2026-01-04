print('Bem vindo a pizzaria')
pizza = input("Selecione o tamanho da sua pizza: p, m, g ")
peperone = input('Você quer Pepenone extra? s ou n ')
queijo = input('Você quer queijo extra? s ou n ')
valor = 0

if pizza == 'p':
  valor += 15
elif pizza == 'm':
  valor += 20
elif pizza == 'g':
  valor += 25
else:
  print('Tamanho de pizza errado, isira p, m ou g')

if peperone == 's':
  if pizza == 'p':
    valor += 2
  elif pizza == 'm' or pizza == 'g':
    valor += 3

if queijo == 's':
  valor += 1

print(f'O valor da pizza é: R$ {valor:.2f}')
