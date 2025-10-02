sal = float(input("Digite o seu salário para descobrir o aumento: R$"))

if sal <= 1250:
    salN = sal*1.15
    print("O salário de R${} agora passa a ser de R${}".format(sal, salN))
else:
    salN = sal*1.10
    print("O salário de R${} agora passa a ser de R${}".format(sal, salN))