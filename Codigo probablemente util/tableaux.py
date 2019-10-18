class Tree(object):
  def __init__(self, lb,iz, der):
    self.left=iz
    self.right=der
    self.label=lb

def Par_Complementario(h):

    #Retorna true si existe un par complementario
    negs= []
    nonegs=[]
    for i in h:
        if i.label == '-':
            negs.append(i.label + i.right.label)
        else:
            nonegs.append(i.label)
    if len(negs)==0 or len(nonegs)==0:
        return False
    for i in negs:
        if i[1] in nonegs:
            return True
        else:
            return False

def LiteralF(A):
    #Dado una formula A, retorna True si A es un literal
    if A.right==None:
        return True
    elif A.label == '-' and A.right.right == None:
        return  True
    else:
        return False

def LiteralL(h):
    #Dado una lista de fórmulas, retorna True si existe
    #al menos un literal
    for i in h:
        if LiteralF(i)== False:
            resul = False
            break
        else:
            resul = True
            continue
    return resul

def Inorder(a):
    if a.right == None:
        return a.label
    elif a.label == "-":
        return "-" + Inorder(a.right)
    elif a.label in ["Y", "O", ">", "<->"]:
        return "("+Inorder(a.left)+a.label+Inorder(a.right)+ ")"

def imprime_hoja(H):
	cadena = "["
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "]"

def Marcar(Lista):

    if len(Lista)==0:
        return "Finalizado"
    else:
        if LiteralL(Lista[0]):
            if Par_Complementario(Lista[0]):
                print(imprime_hoja(Lista[0])+"Cerrada")
                del Lista[0]
                return Marcar(Lista)
            else:
                print(imprime_hoja(Lista[0])+"Abierta")
                del Lista[0]
                return Marcar(Lista)
        else:
            print(imprime_hoja(Lista[0]))
            del Lista[0]
            return Marcar(Lista)

def Sin_Par_Complementario(Lista, pack):
    for formula in Lista:
        if Par_Complementario(formula)==False:
                pack.append(formula)
    return pack

def Clasificacion(A):
    if A.label == "-":
        if A.right.label == "-":
            return "1 Alfa"
        elif A.right.label == "O":
            return "3 Alfa"
        elif A.right.label == ">":
            return "4 Alfa"
        elif A.right.label == "Y":
            return "1 Beta"
    else:
        if A.label == "Y":
            return "2 Alfa"
        elif A.label == "O":
            return "2 Beta"
        elif A.label == ">":
            return "3 Beta"
        
def ejecutar(Lista, pack):
    while len(Lista)>0:
        for h in Lista:
            if not LiteralL(h):
                for formula in h:
                    if not LiteralF(formula):
                        if Clasificacion(formula) == "1 Alfa":
                            h.append([formula.right.right])
                            h.remove(formula)
                        elif Clasificacion(formula) == "2 Alfa":
                            h.append([formula.right, formula.left])
                            h.remove(formula)
                        elif Clasificacion(formula) == "3 Alfa":
                            h.append([Tree('-', None, formula.left),Tree('-', None, formula.right)])
                            h.remove(formula)
                        elif Clasificacion(formula) == "4 Alfa":
                            h.append([formula.left, Tree('-', None, formula.right)])
                            h.remove(formula)
                        elif Clasificacion(formula) == "1 Beta":
                            h.append([Tree('-', None, formula.left)])
                            h.append([Tree('-', None, formula.right)])
                            h.remove(formula)
                        elif Clasificacion(formula) == "2 Beta":
                            h.append([formula.left])
                            h.append([formula.right])
                            h.remove(formula)
                        elif Clasificacion(formula) == "3 Beta":
                            h.append([Tree('-', None, formula.left)])
                            h.append([formula.right])
            else: 
                Sin_Par_Complementario(h, pack)
                Lista.remove(h)





listainterpsverdaderas=[]

p = Tree("p", None, None)
nop = Tree("-", None, p)
nonop = Tree("-", None, nop)
q = Tree("q", None, None)
noq = Tree("-", None, q)
r = Tree("r", None, None)
nor = Tree("-", None, r)
s = Tree("s", None, None)
nos = Tree("-", None, s)
A0=Tree("O", p, q)
noA0 = Tree("-", None, A0)
A1 = Tree(">", r,s)
noA1 = Tree("-", None, A1)
A2 = Tree("Y",noA0, noA1)
noA2 = Tree("-", None, A2)
nonoA2 = Tree("-", None, noA2)
A3 = Tree("O", noA1, q)
noA3 = Tree("-", None, A3)
A4 = Tree(">", r, noA0)
noA4 = Tree("-", None, A4)
a5 = Tree("O", s, q)
A5 = Tree(">", r, a5)
#Marcar([[q], [nop, q], [q, noq], [p, nop]])
#print(LiteralL([nonop, q]))
#sin = Sin_Par_Complementario([[p, q], [nop,p]])
#for hoja in sin:
#    print(imprime_hoja(hoja))
ejecutar([[q],[A0]], listainterpsverdaderas)
