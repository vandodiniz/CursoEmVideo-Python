##EX 1
"""nome = str(input('Qual o seu nome? '))
print(nome.upper())
print(nome.lower())
div = nome.split()
print('O primeiro nome tem {} letras' .format(len(div[0])))
print('O nome completo tem {} letras' .format(len(''.join(div))))"""

##EX 2
"""num = str(input('Digite um numero: '))
esp = num[::-1]
print('Unidades: {}' .format(esp[0]))
print('Dezenas: {}' .format(esp[1]))
print('Centenas: {}' .format(esp[2]))
print('Milhares: {}' .format(esp[3]))"""

##EX3
"""nome = str(input('Digite o nome da cidade: '))
if(nome.find('Santo') == 0):
    print('Começa com Santo')
else:
    print('Não começa com Santo')"""

##EX4
"""nome = str(input('Digite um nome: '))
if('Silva' in nome):
    print("Tem Silva no nome")
else:
    print("Não tem Silva no nome")"""

##EX5
"""frase = str(input('Digite uma frase: '))
print('A frase tem {} letras "a"s' .format(frase.count('a')))
print('A primeira aparece na {}a posição e a ultima na {}a posição'
 .format(frase.find('a')+1, (len(frase) - frase[::-1].find('a'))))"""

#EX6
"""nome = str(input("Digite um nome: "))
esp = nome[::-1]
print("Primeiro nome: {}." .format(nome.split()[0]))
print('último nome: {}' .format(nome[::-1].split()[0][::-1]))"""

