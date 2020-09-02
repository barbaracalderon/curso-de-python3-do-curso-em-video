# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.

cateto_o = int(input("Digite o valor do cateto oposto: "))
cateto_a = int(input("Digite o valor do cateto adjacente: "))
hip = ((cateto_o**2) + (cateto_a**2))**(1/2)
print("O comprimento da hipotenusa é: {}".format(hip))