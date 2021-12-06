#ex1
"""numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
n = int(input('digite um numero: '))
print(f'vc escolheu o numero {numeros[n]}')"""

#ex2
"""nome =''
times = ('Galo', 'palmeiras','flamengo', 'Bragantinho', 'fortaleza', 'corinthians', 'inter' , 'flu' , 'meca', 'cuiaba')
print(times[:5])
print(times[-4:])
for c in range(0,len(times)):
    nome = times[c]
    if nome == 'flu':
        print(f'o flu esta na {c+1} posicao')"""

#ex3
"""from random import randint
n = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print(n)
maior = menor = n[0]
for c in range (0, len(n)):
    if n[c] > maior:
        maior = n[c]
    elif n[c] < menor:
        menor = n[c]
print(menor,' ', maior)"""

#ex4
"""from random import randint
n = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print(n)
print(n.count(9))
print(n.index(3)+1)
for c in n:
    if c%2 == 0:
        print (c, end=' ')"""

#ex5
"""linha = '-'*30
titulo = 'ESTOQUE DE FRUTAS'
itens=('banana', 20, 'maça', 10, 'abacaxi', 15, 'melancia', 40)
print(linha)
print(titulo.center(30))
print(linha)
for c in range(0,len(itens),2):
    print(f'{itens[c]:.<27} {itens[c+1]}')"""

"""#ex6
palavras = ('APRENDER', 'JOGAR', 'ESTUDAR')
for c in palavras:
    print(f'Em {c} temos', end=' ')
    for i in c:
        if i in 'AEIOU':
            print(i, end=' ')
    print('')"""

