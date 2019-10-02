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





p = Tree("p", None, None)
nop = Tree("-", None, p)
nonop = Tree("-", None, nop)
q = Tree("q", None, None)
noq = Tree("-", None, q)
A0=Tree("Y", p, noq)
A = Tree("-", None,A0)
Marcar([[q], [nop, q], [q, noq], [p, nop]])
#print(LiteralL([nonop, q]))