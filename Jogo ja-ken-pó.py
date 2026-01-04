import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

usuario = int(input('O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura: '))
opcoes = [pedra, papel, tesoura]
escolha_cpu = random.randint(0, 2)

if usuario == 0 and escolha_cpu == 1:
  print(f'Jogador: {pedra} \n Computador: {papel} \n você perdeu!!!')
elif usuario == 0 and escolha_cpu == 2:
  print(f'Jogador: {pedra} \n Computador: {tesoura} \n você ganhou!!!')
elif usuario == 1 and escolha_cpu == 0:
  print(f'Jogador: {papel} \n Computador: {pedra} \n você ganhou!!!')
elif usuario == 1 and escolha_cpu == 2:
  print(f'Jogador: {papel} \n Computador: {tesoura} \n você perdeu!!!')
elif usuario == 2 and escolha_cpu == 0:
  print(f'Jogador: {tesoura} \n Computador: {pedra} \n você perdeu!!!')
elif usuario == 2 and escolha_cpu == 1:
  print(f'Jogador: {tesoura} \n Computador: {papel} \n você ganhou!!!')
elif usuario == escolha_cpu:
  print(f'\nEmpate! Ambos escolheram {opcoes[usuario]} \n Jogue novamente!!!')
else:
  print('Você digitou um numero invalido, jogue novamente!!!')
