from math import hypot
cO = float(input("Comprimento do cateto oposto: "))
cA = float(input("Comprimento do cateto adjacente: "))
hip = hypot(cA, cO)
print("A hipotenusa vai medir {:.2f}".format(hip))