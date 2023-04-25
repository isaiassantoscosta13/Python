#Exercício JokenPO
import random
from time import sleep

opc = ['pedra', 'papel', 'tesoura']
print("\n")
print("Suas opções: \n" +
      "[0] PEDRA \n" +
      "[1] PAPEL \n" +
      "[2] TESOURA \n"
)
maquina = random.choice(opc).upper()

jog = int(input("Qual a sua jogada ? "))

print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PÔ!!!')
sleep(1)
 
print("A máquina jogou {}".format(maquina))

if jog == 0:
    if maquina == 'PEDRA':
        print("O jogo ficou EMPATE.")
        print("Ambos jogaram PEDRA.")
    elif maquina == 'PAPEL':
        print("Você PERDEU !!!")
        print("PAPEL ganha de PEDRA.")
    elif maquina == 'TESOURA':
        print("Você GANHOU !!!")
        print("PEDRA ganha de TESOURA.")

elif jog == 1:
    if maquina == 'PAPEL':
        print("O jogo ficou EMPATE.")
        print("Ambos jopgaram PAPEL.")
    elif maquina == 'PEDRA':
        print("Você GANHOU !!!")
        print("PAPEL ganha de PEDRA.")
    elif maquina == 'TESOURA':
        print("Você PERDEU !!!")
        print("TESOURA ganha de PAPEL.")

elif jog == 2:
    if maquina == 'TESOURA':
        print("O jogo ficou EMPATE.")
        print("Ambos jopgaram TESOURA.")
    elif maquina == 'PAPEL':
        print("Você GANHOU !!!")
        print("TESOURA ganha de PAPEL.")
    elif maquina == 'PEDRA': 
        print("Você PERDEU !!!")
        print("PEDRA ganha de TESOURA.")
else: 
    print("Opção inválida !!!")

print("\n")