# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site do pudim não está disponível :(\033[m')
else:
    print('\033[32mO site do pudim está no ar! :)\033[m')