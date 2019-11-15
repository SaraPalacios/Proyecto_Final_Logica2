def voidclaus(U):
    for i in range(len(U)):
        if len((U[i])) == 0:
            return True
        else:
            return False
def tieneclausulaunit(U):
    #verdadero si contiene una clausula unitaria
    res = (False, ' ')
    for i in range(len(U)):
        if len(U[i]) == 1:
            res = (True, U[i])
            break
        elif len(U[i]) == 2 and U[i][0] == '-':
            res = (True, U[i])
            break
    return res

def complem(L):
    if len(L) == 1:
        return '-'+ L
    else:
       return L.replace('-', '')
def is_neg(L):
    if L[0] == '-':
        return True
    else:
        return False 
def remove_clausuni(S, cuni):
    S.remove(cuni)
    for elem in S:
        if complem(cuni) in elem:
            res = elem.replace(complem(cuni),'')
            S.remove(elem)
            S.append(res)
    for el in S:
        if cuni in el:
            S.remove(el)
    return S, cuni

def unit_prop(S, I):
    while tieneclausulaunit(S)[0] and voidclaus(S) == False:
        if is_neg(tieneclausulaunit(S)[1]):
            I[tieneclausulaunit(S)[1]] = 0

        else:
            I[tieneclausulaunit(S)[1]] = 1 
    
        remove_clausuni(S, tieneclausulaunit(S)[1])
    return S, I


def DPLL(S, I):
    sol = unit_prop(S,I)
    if voidclaus(sol[0]):
        return "insatisfacible", {}
    if len(sol[0])==0:
        return "Satisfacible", sol[1]



s = ["p", "-pq-r", "q"]


print(DPLL(s,{}))