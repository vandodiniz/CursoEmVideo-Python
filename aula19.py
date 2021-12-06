#ex1
'''boletim = dict()
boletim['aluno'] = input('Nome: ')
boletim['nota'] = int(input('Nota: '))
if boletim['nota'] >= 7:
    boletim['situação'] = 'Aprovado'
elif 7>boletim['nota']>=5:
    boletim['situação'] = 'Rec'
else:
    boletim['situação'] = 'Reprovado'
for k,v in boletim.items():
    print(f'{k} {v}')'''

#ex2
'''from random import randint
memoria = list()
info = dict()
for c in range(0,4):
    info['id'] = c
    info['score'] = randint(1,6)
    memoria.append(info.copy())
    print(f'Jogador {c} tirou {info["score"]}')
print(memoria[0])'''

#ex3
"""ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['nasc'] = int(input('ano de nascimento: '))
ficha['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['carteira'] >0:
    ficha['cont'] = int(input('Ano de contratação: '))
    ficha['sal'] = int(input('Salario: '))
    ficha['apos'] = ficha['nasc'] + 40
for c, k in ficha.items():
    print(f'{c} = {k}')"""

#ex4
'''ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['gols'] = list()
soma = 0
for c in range (0,5):
    gol = int(input(f'Quantos gols na partida {c+1}: '))
    ficha['gols'].append(gol)
    soma += gol
ficha['total'] = soma

print(ficha, '\n')

for c,k in ficha.items():
    print(f'o campo {c} tem valor {k}')
print('\n')

print(f'o jogador {ficha["nome"]} jogou 5 partidas.')
for c in range(0,5):
    print(f'- Na partida {c+1}, fez {ficha["gols"][c]} gols')
print(f'Foram feitos {ficha["total"]} gols no total')'''

#ex5
'''pessoas = list()
dados = dict()
total = 0
media = 0
while True:
    dados['Nome'] = input('Nome: ')
    dados['Sexo'] = input('Sexo: ')
    while dados['Sexo'] not in 'MmHh':
        dados['Sexo'] = input('Erro, responda apenas M ou H. \nSexo: ')
    dados['Idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    total +=1
    media += dados['Idade']
    dados.clear()

    op = input('Quer continuar? [S/N]')
    while op not in 'sSnN':
        op = input('Erro, responda apenas S ou N. Quer continuar? [S/N]')
    if op in 'nN':
        break
media = media/total
print(pessoas)
print(total)
print(media)
for c in pessoas:
    if c['Sexo'] in 'Mm':
     print(vc, end=' ')
print('\n')
for c in pessoas:
    if c['Idade'] > media:
        print(c, end=' ')'''

#ex6



    


