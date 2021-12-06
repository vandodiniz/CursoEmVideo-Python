#EX1
"""import random
n1 = int(random.randrange(0,5))
n2 = int(input('Digite um numero: '))
if(n1==n2):
    print("Parabéns, vc acertou")
else:
    print("O computador ganhou, o numero certo era {}" .format(n1))"""

#ex2
"""vel = int(input('digite a velocidade: '))
if(vel <= 80):
    print('Velocidade permitida')
else:
    print('Infração de trânsito! Multa de R${},00' .format((vel-80)*7))"""

#ex3
"""n = int(input('digite um numero: '))
if(n%2 == 0):
    print('par')
else:
    print('impar')"""

#ex4
"""km = int(input('digite um numero: '))
if(km<=200):
    preço = km*0.5
else:
    preço = km*0.45
print('Valor da viagem: R${:.2f}' .format(preço))"""

#ex5
"""n = int(input('digite um ano: '))
if((n%4 == 0 and n%100!=0) or (n%400==0)):
    print('bissexto')
else:
    print('n bissexto')"""

#ex6
"""n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
if(n1>n2):
    maior = n1
else:
    maior = n2
if(n3>=maior):
    maior = n3
print('O maior numero é {}' .format(maior))"""