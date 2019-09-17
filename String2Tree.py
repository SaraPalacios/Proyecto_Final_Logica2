import Class_Tree as T

def String2Tree(A, LetrasProposicionales):
    #Crea una formula como tree dado una formula en NPI
    #Input: A, lista de caracteres en NPI
    #Output: Formula como Tree
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in LetrasProposicionales:
            pila.append(T.Tree(c, None, None))
        elif c == '-':
            FormulaAux = T.Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(FormulaAux)
        elif c in conectivos:
            FormulaAux = T.Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(FormulaAux)

    return pila[-1]
    
