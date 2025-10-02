ano = int(input("Digite o ano que gostaria de saber se é bissexto: "))

if ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))
elif ano % 4 == 0 and ano % 100 != 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))