class Tree(object):
  def __init__(self, lb,iz, der):
    self.left=iz
    self.right=der
    self.label=lb
def String2Tree(A, LetrasProposicionales):
    #Crea una formula como tree dado una formula en NPI
    #Input: A, lista de caracteres en NPI
    #Output: Formula como Tree
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in LetrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            FormulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(FormulaAux)
        elif c in conectivos:
            FormulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(FormulaAux)

    return pila[-1]

def Inorder(a):
    if a.right == None:
        return a.label
    elif a.label == "-":
        return "-" + Inorder(a.right)
    elif a.label in ["Y", "O", ">", "<->"]:
        return "("+Inorder(a.left)+a.label+Inorder(a.right)+ ")"

def V(f, I):
    if f.right == None:
        return I[f.label]
    elif f.label == '-':
        return 1 - V(f.right,I)
    elif f.label == 'Y':
        return V(f.left,I)*V(f.right,I)
    elif f.label == 'O':
        return max(V(f.left,I), V(f.right,I))
    elif f.label == '>':
        return max(1-V(f.left,I), V(f.right,I))
    elif f.label == '<->':
        return 1 - (V(f.left,I)-V(f.right,I))**2

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


print(conjunciones)
interps = []
aux = {}
for a in LetrasProposicionales:
    aux[a] = 1 #se inicializan las interpretaciones como verdaders
interps.append(aux) #se crea la lista con todas las interpretaciones
for a in LetrasProposicionales:
    interps_aux = [i for i in interps]
    for i in interps_aux:
        aux1 = {}
        for b in LetrasProposicionales:
            if a == b:
                aux1[b] = 1- i[b] #cambia el valor de verdad de b
            else:
                aux1[b] = i[b] #mantiene el valor de verdad para las demas
        interps.append(aux1)

A = String2Tree(conjunciones,LetrasProposicionales)
Af=Inorder(A)

soluciones=[]
for i in interps:
    if V(A, i) == 1:
        soluciones.append(i)

print(len(soluciones))
keys = list(soluciones[0].keys())
valores = list(soluciones[0].values())
form=[]
for i in soluciones[0]:
    if soluciones[0][i] == 0:
        form.append("-"+i)
    else:
        form.append(i)

"""for l in form:
    if '-' not in l:
        print(l)
"""