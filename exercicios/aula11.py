#ex1
"""casa = float(input('qual o valor da  casa: '))
sal = float(input('digite seu salario: '))
t = int(input('digite o tempo estipulado: '))
pres = casa/(12*t) 
if(pres>0.3*sal):
    print('prestaçao de {:.2f}. Emprestimo negado' .format(pres))
else:
    print('prestaçao de {:.2f}. Emprestimo aprovado' .format(pres))"""

#ex2
'''n = int(input('Digite um numero: '))
esc = int(input("""Escolha pra qual bsae vc quer convertê-lo\n
1) Binario\n2) Octal\n3) Hexa\n\n"""))
if(esc == 1):
    res = bin(n)
    print('Conversão = {}' .format(res))
elif(esc == 2):
    res = oct(n)
    print('Conversão = {}' .format(res))
elif(esc == 3):
    res = hex(n)
    print('Conversão = {}' .format(res))
else:
   print ('escolha inválida!')'''

#ex3
"""n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
if(n1>n2):
    print('o PRIMEIRO numero é maior')
elif(n1<n2):
    print('o SEGUNDO numero é maior')
else:
    print('os dois numeros sao iguais')"""

#ex4    
"""ano = int(input('digite seu ano de nascimento: '))
id = 2021 - ano
if(id >18):
    print('vc está {} anos atrasados para o alistamento' .format(id-18))
elif(id==18):
    print('vc está na hora de alistar')
else:
    print('faltam {} anos pra seu alistamento' .format(18-id))"""

#ex5
"""n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
if(n1>n2+n3 or n2>n1+n3 or n3>n1+n2):
    print('nao eh trinagulo')
elif(n1==n2 and n1==n3):
    print('EQUILATERO')
elif(n1!=n2 and n1!=n3 and n2!=n3):
    print('ESCALENO')
else:
    print('isosceles')"""

#ex6
import random
comp = int(random.randrange(1,4))
print('''escolha sua jogada
1) tesoura
2) papel
3) pedra ''')
vc = int(input('escolha: '))
if(vc==1):
    if(comp==1):
        print('O computador também escolheu tesoura! EMPATE')
    if(comp==2):
        print('O computador escolheu papel! VITÓRIA')
    if(comp==3):
        print('O computador escolheu pedra! DERROTA')
elif(vc==2):
    if(comp==2):
        print('O computador também escolheu papel! EMPATE')
    if(comp==1):
        print('O computador escolheu tesoura! DERROTA')
    if(comp==3):
        print('O computador escolheu pedra! VITORIA')
elif(vc==3):
    if(comp==3):
        print('O computador também escolheu pedra! EMPATE')
    if(comp==1):
        print('O computador escolheu tesoura! VITORIA')
    if(comp==2):
        print('O computador escolheu papel! DERROTA')
else:
    print('escolha invalida')
