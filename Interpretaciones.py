letrasProp = ['p', 'q', 'r']
interps = []
aux = {}
for a in letrasProp:
    aux[a] = 1 #se inicializan las interpretaciones como verdaders

interps.append(aux) #se crea la lista con todas las interpretaciones

for a in letrasProp:
    interps_aux = [i for i in interps]
    for i in interps_aux:
        aux1 = {}
        for b in letrasProp:
            if a == b:
                aux1[b] = 1- i[b] #cambia el valor de verdad de b
            else:
                aux1[b] = i[b] #mantiene el valor de verdad para las demas
        interps.append(aux1)

if __name__ == "__main__":
    print("Interpretaciones: ")
        for i in interps:
            print(i)

