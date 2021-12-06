#ex1
"""s=0
while(True):
    n = int(input('digite um numero: '))
    if(n==999):
        break
    s+=n
print(s)"""

#ex2
"""while(True):
    n = int(input('digite um numero: '))
    if(n<0):
        break
    for c in range(0,10):
        print(f'{n}*{c} = {n*c}')"""

#ex3
"""from random import randint
o = cont = 0
while(True):
    while(o!=1 and o!=2):
        o = int(input('[1] Par\n[2] Impar\n '))
        
    n = int(input('digite um numero: '))
    c = randint(0,9)
    s = n+c
    if(o==1):
        if(s%2==0):
            cont+=1
        else:
            print(f"A soma deu {s}. Vc perdeu com {cont} vitorias")
            break
    else:
        if(s%2==1):
            cont+=1
        else:
            print(f"A soma deu {s}. Vc perdeu com {cont} vitorias")
            break"""

#ex4
"""conti=conth=contm=0
while(True):
    nome = str(input("Nome: "))
    id = int(input("Idade: "))
    sexo = str(input('Digite seu sexo [H/M]: ')).upper()
    while (sexo!='H' and sexo!='M'):
        sexo = str(input("Sexo inválido! Digite novamente: "))
    if(id>18):
        conti+=1
    if(sexo=='H'):
        conth+=1
    if(sexo=='M' and id <20):
        contm+=1
    op = input('Deseja adicionar mais? [S/N]: ').upper()
    if(op=='N'):
        break
print(f'{conti} {conth} {contm}')"""

#ex5
"""nomeM = ''
menor = 9999999999
cont = soma = 0
while True:
    nome = str(input('Nome: '))
    p = float(input('Preço: '))
    soma += p
    if(p>1000):
        cont+=1
    if(p<menor):
        menor = p
        nomeM = nome
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if op == 'N':
        break
print(f'Total gasto: {soma:.2f}\nMais de 1000 reais: {cont}\nMais barato: {nomeM}')"""

#ex6
n = int(input('valor: '))
cinq = n//50
n = n%50
v = n//20
n = n%20
d = n//10
u = n%10
print(f'{cinq} {v} {d} {u}')


