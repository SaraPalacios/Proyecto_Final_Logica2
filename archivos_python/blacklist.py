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

LetrasProposicionales = ["NAY", "E-B-Y", "A-E-Y", "A-SY", "S-NY", "N-S-CYY",
                "CLY", "BEY", "SMY", "A", "APJYY", "PC-B-MYYY", "HKBYY", 
                "S-E-L-M-F-DYYYYY", "N-LCMYYY", "BGY"]

conjunciones = ' '
inicial = True
#Creación de la fórmula en notacion polaca inversa para resolver el enigma
for p in LetrasProposicionales:
    aux1 = [x for x in LetrasProposicionales if x!= p]
    for q in aux1:
        aux2 = [x for x in aux1 if x!= q]
        for r in aux2:
            aux3 = [x for x in aux2 if x!= r]
            for s in aux3:
                aux4 = [x for x in aux3 if x!= s]
                for t in aux4:
                    aux5 = [x for x in aux4 if x!= t]
                    for u in aux5:
                        literal = u + t + s + r + q + p +'Y'+'Y'+'Y'+'Y'+'Y'
                        aux6 = [x + '-' for x in aux5 if x!= u]
                        for v in aux6:
                            literal = v + literal + 'Y'
                        if inicial:
                            conjunciones = literal
                            inicial = False
                        else:
                            conjunciones = literal+conjunciones+ 'O'
