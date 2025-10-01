
#Solução Minha
'''nome = input("Qual é o seu nome completo? ")
ver = nome.upper().find('SILVA')
print("Seu nome tem Silva? {}".format(ver != -1))'''

#Solução Guanabara
nome = input("Qual é o seu nome completo? ").strip()
print("Seu nome tem Silva? {}".format('silva' in nome.lower()))