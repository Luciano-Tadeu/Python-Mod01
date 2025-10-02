import random
from time import sleep

print("-=--"*30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=--"*30)

num = random.randint(0, 5)

numD = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(2)

if num == numD:
    print("PERDI! Eu pensei no número {} mesmo!".format(num))
else:
    print("GANHEI! Eu pensei no número {} e não no {}".format(num, numD))