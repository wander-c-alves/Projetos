print('Compre seu ingresso')
alt = (int(input('Qual a sua altura? ')))
conta = 0
if alt >= 120:
  print('Você pode comprar o ingresso! ')
  idade = int(input('Digite su idade: '))
  if idade <= 12:
    conta = 5
    print('Seu ingresso cuta R$ 5')
  elif idade >= 18 and idade < 45:
    conta = 18
    print('Seu ingresso cuta R$ 18')
  elif idade > 13 and idade < 18:
    conta = 9
    print('Seu ingresso cuta 9')
  elif idade >= 45 and idade <= 55:
    conta = 0
    print('seu ingresso é gratis')

  com_foto = input('Se quiser uma foto, digite s, caso contrario, digite n ')
  if com_foto == 's':
    conta += 3
  print(f'O valor final é R$ {conta}')
else:
  print('Você não pode comprar o ingresso! ')
