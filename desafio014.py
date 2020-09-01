# Escreva um programa que converta uma temperatura
# digitada em Celsius e converta para Farenheit.

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = ((celsius/5)*9)+32
print('A temperatura de {:.1f} Celsius corresponde a {:.1f} Fahrenheit.'.format(celsius, fahrenheit))