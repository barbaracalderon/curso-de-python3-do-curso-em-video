# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

#importar a biblioteca toda; agora precisa usar 'math.função-de-sejada()'
import math
angulo = float(input("Digite um ângulo: "))
#converte o ângulo X de graus para radianos
angulo_rad = math.radians(angulo)
#os cálculos
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print("O âgulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.".format(angulo, seno, cosseno, tangente))

