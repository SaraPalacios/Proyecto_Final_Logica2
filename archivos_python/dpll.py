def voidclaus(U):
    #Retrona verdadero si existe una cláusula vacía
    for i in range(len(U)):
        if len((U[i])) == 0:
            return True
        else:
            return False
def tieneclausulaunit(U):
    #verifica si un conjunto tiene o no una cláusula unitaria
    #si la tiene retorna true junto con la cláusula
    #si no retorna false y ' '
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
    #Calcula el complemento de un literal
    if len(L) == 1:
        return '-'+ L
    else:
       return L.replace('-', '')
def is_neg(L):
    #verifica si  el literal L es -L o L
    if L[0] == '-':
        return True
    else:
        return False 
  
#SUBRUTINA unitPropagate:
# input: S, conjunto de cláusulas. I, interpretación parcial
# Output: S, conjunto de cláusulas. I, interpretación parcial 
def unit_prop(S, I):
    sp = S.copy()
    while tieneclausulaunit(sp)[0]  and voidclaus(sp) == False:
        claus = tieneclausulaunit(sp)[1]
        c = complem(claus)
        if claus[0]!='-':
            sp.remove(claus)
            for el in S:
                if c in el:
                    res = el.replace(c, '')
                    sp.remove(el)
                    sp.append(res)
            for el in S:
                if el in sp:
                    if claus in el:
                        sp.remove(el)
            if is_neg(claus):
                I[complem(claus)] = 0
            elif(is_neg(claus) == False):
                I[claus] = 1
        else:
            sp.remove(claus)
            for el in S:
                if el in sp:
                    if claus in el:
                        sp.remove(el)
            for el in sp:
                if c in el:
                    res = el.replace(c, '')
                    sp.remove(el)
                    sp.append(res)
            if is_neg(claus):
                I[complem(claus)] = 0
            elif(is_neg(claus) == False):
                I[claus] = 1         
    return sp, I

#Algoritmo DPLL:
#Input: S, conjunto de cláusulas. I, interpretación parcial
#Output: Satisfacible/insatisfacible. I, interpretación parcial
def DPLL(S, I):
    s,i = unit_prop(S,I)
    if voidclaus(s):
        return "insatisfacible", {}
    if len(s)==0:
        return "Satisfacible", i

    l = s[0][0]
    sp = s.copy()
    Ip = i.copy()
    if l != '-':
        c = complem(l)
        for el in s:
            if c in el:
                res = el.replace(c,'')
                sp.remove(el)
                sp.append(res)
        for el in s:
            if el in sp:
                if l in el:
                    sp.remove(el)
        Ip[l]=1
        s2,i1 = DPLL(sp,Ip)
        if s2=="Satisfacible":
            return "Satidsfacible", i1
        else:
            s_seg = s.copy()
            i_seg = i.copy()
            c = complem(l)
            for element in s:
                if c in element:
                    s_seg.remove(element)
            for el in s_seg:
                if l in el:
                    res = el.replace(l,'')
                    s_seg.remove(el)
                    s_seg.append(res)
            i_seg[l] = 0
            return DPLL(s_seg,i_seg)
    else: 
        l = l+s[0][1]
        c = complem(l)
        for elem in s:
            if l in elem:
                res = elem.replace(l,'')
                sp.remove(elem)
                sp.append(res)
        for el in s:
            if el in sp:
                if c in el:
                    sp.remove(el)    
        Ip[l]=0
        s2,i1 = DPLL(sp,Ip)
        if s2=="Satisfacible":
            return "Satidsfacible", i1
        else:
            s_seg = s.copy()
            i_seg = i.copy()
            c = complem(l)   
            for el in s:
                if l in el:
                    res = el.replace(l,'')
                    s_seg.remove(el)
                    s_seg.append(res)
            for el in s:
                if el in s_seg:
                    if c in el:
                        s_seg.remove(el)
            i_seg[l]=1
            return DPLL(s_seg,i_seg)
    
s = ["p-qr", "-pq-r", "-p-qr", "-p-q-r"]


print(DPLL(s,{}))