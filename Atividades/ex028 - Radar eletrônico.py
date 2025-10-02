vel = int(input("Qual a velocidade do carro? "))
if vel <= 80:
    print("Dirija com segurança! Tenha um bom dia!")
else:
    multa = (vel - 80) * 7
    print("Você excedeu o limite de 80km/h e foi MULTADO! No valor de R${:.2f}".format(float(multa)))