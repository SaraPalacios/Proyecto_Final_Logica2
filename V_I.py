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
def val(f,L):
    auxi = []
    for i in L:
        auxi.append(V(f,i))
    if 1 not in auxi:
        return "Formula insatisfacible"
    elif 0 not in auxi:
        return "Formula valida"
    elif 1 and 0 in auxi:
        return "Formula contingente"


