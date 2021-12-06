import math

##ex16
#n = float(input('Digite um numero: '))
#print('Valor inteiro: {}' .format(math.trunc(n)))

'''##ex17
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
print("hipo = {}" .format(math.sqrt(n1**2+n2**2)))'''

'''##ex18
n1 = float(input('Digite um angulo: '))
print("seno = {:.2f}\ncos = {:.2f}\ntan = {:.2f}" .format(math.sin(math.radians(n1)),math.cos(math.radians(n1)),math.tan(math.radians(n1))))'''

##ex19

import random
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))
candidatos = [n1,n2,n3,n4]
print('O sorteado foi {}' .format(random.choice(candidatos)))
random.shuffle(candidatos)
print('A ordem foi {}' .format(candidatos))
