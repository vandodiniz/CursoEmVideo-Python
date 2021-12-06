import modulo

while True:
    modulo.menu()
    op = modulo.escolha()
    if   op==1:
        modulo.listaPokemon()
    elif op==2:
        modulo.adicionaPokemon()
    elif op==3:
        modulo.cabeçalho('FIM DO PROGRAMA!')
        break
