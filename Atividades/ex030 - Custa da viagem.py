viagem = int(input("Qual a distância da sua viagem? "))

if viagem <= 200:
    valor = viagem*0.50
    print("O valor da viagem será de R${}".format(valor))
elif viagem < 0:
    print("Valor inválido")
else:
    valor = viagem*0.45
    print("O valor da viagem será de R${}".format(valor))