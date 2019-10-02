LetrasProposicionales = [str(i) for i in range(1,10)] #creacion de letras prop
conjunciones = ' '
inicial = True

for p in LetrasProposicionales:
    aux1 = [x for x in LetrasProposicionales if x!= p]
    for q in aux1:
        aux2 = [x for x in aux1 if x!= q]
        for r in aux2:
            literal = r + q + p + 'Y' + 'Y'
            aux3 = [x + '-' for x in aux2 if x!= r]
            for k in aux3:
                literal = k + literal + 'Y'
            if inicial:
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'

                
