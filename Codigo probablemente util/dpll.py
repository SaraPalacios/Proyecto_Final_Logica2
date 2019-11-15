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
    l = sol[0][0][0]
    sp = S.copy()
    Ip = I.copy()
    if l != '-':
        for elem in sp:
            if complem(l) in elem:
                res = elem.replace(complem(l),'')
                sp.remove(elem)
                sp.append(res)
        for el in sp:
            if l in el:
                sp.remove(el)
        Ip[l]=1
        Ip[complem(l)] = 0
    else: 
        for elem in sp:
            if l in elem:
                res = elem.replace(l,'')
                sp.remove(elem)
                sp.append(res)
        for el in S:
            if l[1] in el:
                sp.remove(el)
       
        Ip[l]=0
        Ip[complem(l)]=1
    sol2 = DPLL(sp,Ip)
    if sol2[0]=="Satisfacible":
        return "Satidsfacible", Ip
   
    

s = ["p", "-pq", "-qrs"]


print(DPLL(s,{}))