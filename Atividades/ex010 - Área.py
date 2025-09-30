l = float(input('Largura da parede: '))
a = float(input("Altura da parede: "))
area = l*a
litros = area/2
print("Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m² \nPara pintar essa parede você precisará de {:.2f}l de tinta.".format(l, a, area, litros))