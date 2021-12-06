def aumentar(x,y, con=False):
    res = x+y
    if con==True:
        res = moeda(res)
    return res

def diminuir(x,y, con=False):
    res = x-y
    if con==True:
        res = moeda(res)
    return res

def dobro(x, con=False):
    res = x*2
    if con==True:
        res = moeda(res)
    return res

def metade(x, con=False):
    res = x/2
    if con==True:
        res = moeda(res)
    return res

def moeda(x):
    return f'R${x:.2f}'

def resumo(p, a, d):
    print(moeda(p+a))
    print(moeda(p-d))
    print(moeda(p*2))
    print(moeda(p/2))

