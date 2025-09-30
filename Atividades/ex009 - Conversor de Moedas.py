din = float(input("Quanto dinheiro você possui? R$"))
dinUSD = din*0.19
print("Com R${} você pode comprar US${:.2f}".format(din, dinUSD))