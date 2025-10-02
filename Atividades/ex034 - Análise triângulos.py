print("-="*20)
print("Analisador de Triângulos")
print("-="*20)

a = float(input("Segmento 1: "))
b = float(input("Segmento 2: "))
c = float(input("Segmento 3: "))

if a + b > c and a + c > b and b + c > a:
    print("É um triângulo válido!")
else:
    print("Não é um triângulo válido!")