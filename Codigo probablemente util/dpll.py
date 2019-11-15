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

def remv_lite(S, lit):
    for elem in S:
        if complem(lit) in elem:
            res = elem.replace(complem(lit),'')
            S.remove(elem)
            S.append(res)
    for el in S:
        if lit in el:
            S.remove(el)



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
        remv_lite(sp,l)
        Ip[l]=1
        Ip[complem(l)] = 0
    else: 
        l = '-'+sol[0][0][1]
        for elem in sp:
            if l in elem:
                res = elem.replace(l,'')
                sp.remove(elem)
                sp.append(res)
        for el in sp:
            if l[1] in el:
                sp.remove(el)
       
        Ip[l]=0
        Ip[complem(l)]=1
    sol2 = DPLL(sp,Ip)
    if sol2[0]=="Satisfacible":
        return "Satidsfacible", Ip
    else:
        s3 = sol[0].copy()
        I3 = I.copy()
        if l!='-':
            for el in s3:
                if l in el:
                    res = el.replace(l,'')
                    s3.remove(el)
                    s3.append(res)
            for el in s3:
                if complem(l) in el:
                    s3.remove(el)
            I3[l]=0
            I3[complem(l)]=1
        else:
            l =sol[0][0][1]
            for el in s3:
                if '-'+l in el:
                    res = el.replace('-'+l,'')
                    s3.remove(el)
                    s3.append(res)
            for el in s3:
                if complem('-'+l) in el:
                    s3.remove(el)

            I3[l]= 1
            I3[complem(l)] = 0
        sol3 = DPLL(s3,I3)
        return sol3


s = ["p-qr", "-pq-r", "-p-qr", "-p-q-r"]


print(DPLL(s,{}))