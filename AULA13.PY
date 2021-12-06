#ex1
"""sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while (sexo!='M' and sexo!='F'):
    sexo = str(input("Sexo inválido! Digite novamente: "))
print("Sexo registrado com sucesso!")"""

#ex2
"""from random import randint
comp = randint(0,10)
print(comp)
cont = 1
esc = int(input("Escolha um número de 0 a 10: "))
while esc!=comp:
    cont+=1
    esc = int(input("Vc errou o número! Tente novamente: "))
print("Parabéns, vc acertou na {}a tentativa" .format(cont)) """

#ex3
'''n = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
esc = 0
while esc!=7:
    esc = int(input("""[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Comparação
[6] Novos números
[7] Sair
Escolha uma opção: """))
    if(esc==1):
        print("O resultado é {}" .format(n+n2))
    elif(esc==2):
        print("O resultado é {}" .format(n-n2))
    elif(esc==3):
        print("O resultado é {}" .format(n*n2))
    elif(esc==4):
        print("O resultado é {}" .format(n/n2))
    elif(esc==5):
        maior = n
        if(n2>n):
            maior = n2
        print("O maior número é o {}" .format(maior))
    elif(esc==6):
        n = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
    elif(esc==7):
        print("Obrigado pela preferencia!")
    else: 
        print("Opção inválida! Digite novamente")'''

#EX4
"""n = int(input('Digite um número: '))
fat = 1
c = 0
while c <= n:
    if c==0:
        fat = fat*1
    else:
        fat = fat * c
    c+=1
print('fatorial: {}' .format(fat))    """    

#ex5
"""n = int(input('digite um numero: '))
r = int(input('digite a razao: '))
ele = n
i=0
while(i<10):
    print(ele, end=' ')
    ele = ele + r
    i+=1"""

#ex6
"""n = int(input('digite um numero: '))
r = int(input('digite a razao: '))
ele = n
lim = 10
i=0
sair = 0
while (i<=lim):
    print(ele, end=' ')
    ele = ele + r
    if(i==lim):
        lim = int(input("quantos termos vc quer mostrar?: ")) + i
    i+=1"""

#ex7
"""n = int(input('digite um numero: '))
n1 = 0
n2 = 1
i=0
while(i<n):
    if(i==0):
        print(n1, end=' ')
    elif(i==1):
        print(n2, end=' ')
    else:
        ele = n1+n2
        print(ele, end=' ')
        n1 = n2
        n2 = ele
    i+=1"""

#ex 8
"""sair = 0
soma = 0
while (sair==0):
    n = int(input('digite um numero: '))
    if(n==999):
        sair = 1
    else:
        soma = soma + n
print(soma)"""
