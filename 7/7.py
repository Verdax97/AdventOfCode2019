f = open("7.txt","r")
lista = f.read()
temp = lista.split(",")
f.close()
temp = list(map(int, temp))
stati = [0,1,2,3,4]
uscite = [0,0,0,0,0]
soluzioni = []
nastri = [[],[],[],[],[]]
contatori = [0,0,0,0,0]
alt = [0,0,0,0,0]
coso = True
def computa(nAmplificatore, stato, ricevuto):
    cont = 0
    nexto = cont
    arr = temp[:]
    primotre = True
    while arr[cont] != 99:
        val = [0,0,0]
        mode1 = 0
        mode2 = 0
        mode3 = 0
        if len(str(arr[cont])) > 2:
            opcode = int(str(arr[cont])[-2:])
            mode1 = int(str(arr[cont])[-3])
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if len(str(arr[cont])) > 3:
                mode2 = int(str(arr[cont])[-4])
                if mode2 == 0:
                    val[1] = arr[arr[cont + 2]]
                else:
                    val[1] = arr[cont + 2]
                if len(str(arr[cont])) > 4:
                    mode3 = int(str(arr[cont])[-5])
                    if mode3 == 0:
                        val[2] = arr[arr[cont + 3]]
                    else:
                        val[2] = arr[cont + 3]
        else:
            opcode = arr[cont]
        if opcode == 1:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            arr[arr[cont + 3]] = val[0] + val[1]
            nexto = cont + 4
        elif opcode == 2:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            arr[arr[cont + 3]] = val[0] * val[1]
            nexto = cont + 4
        elif opcode == 3:
            #valin = int(input())
            if primotre == True:
                valin = stato
                primotre = False
            else:
                valin = ricevuto
            arr[arr[cont + 1]] = valin
            nexto = cont + 2
        elif opcode == 4:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            uscite[nAmplificatore] = val[0]
            #print("Output: ", val[0])
            nexto = cont + 2
        elif opcode == 5:#jump if true val[0]!= 0
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            nexto = cont + 3
            if val[0] != 0:
                nexto = val[1]
        elif opcode == 6:#jump if false val[0]== 0
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            nexto = cont + 3
            if val[0] == 0:
                nexto = val[1]
        elif opcode == 7:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            if val[1] > val[0]:
                arr[arr[cont+3]] = 1
            else:
                arr[arr[cont+3]] = 0
            nexto = cont + 4
        elif opcode == 8:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            if val[1] == val[0]:
                arr[arr[cont+3]] = 1
            else:
                arr[arr[cont+3]] = 0
            nexto = cont + 4
        else:
            print("problema", opcode)
            exit()
        if nexto > len(arr):
            print("interrotto")
            break
        else:
            cont = nexto
    return (arr[0])

def computaConRiserva(nAmplificatore, stato, ricevuto):
    cont = 0
    cont = contatori[nAmplificatore]
    nexto = cont
    arr = nastri[nAmplificatore]
    primotre = True
    while arr[cont] != 99:
        val = [0,0,0]
        mode1 = 0
        mode2 = 0
        mode3 = 0
        if len(str(arr[cont])) > 2:
            opcode = int(str(arr[cont])[-2:])
            mode1 = int(str(arr[cont])[-3])
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if len(str(arr[cont])) > 3:
                mode2 = int(str(arr[cont])[-4])
                if mode2 == 0:
                    val[1] = arr[arr[cont + 2]]
                else:
                    val[1] = arr[cont + 2]
                if len(str(arr[cont])) > 4:
                    mode3 = int(str(arr[cont])[-5])
                    if mode3 == 0:
                        val[2] = arr[arr[cont + 3]]
                    else:
                        val[2] = arr[cont + 3]
        else:
            opcode = arr[cont]
        if opcode == 1:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            arr[arr[cont + 3]] = val[0] + val[1]
            nexto = cont + 4
        elif opcode == 2:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            arr[arr[cont + 3]] = val[0] * val[1]
            nexto = cont + 4
        elif opcode == 3:
            #valin = int(input())
            if primotre == True and coso == True:
                valin = stato
                primotre = False
            else:
                valin = ricevuto
            arr[arr[cont + 1]] = valin
            nexto = cont + 2
        elif opcode == 4:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            nastri[nAmplificatore] = arr[:]
            uscite[nAmplificatore] = val[0]
            #print("Output: ", val[0])
            nexto = cont + 2
            contatori[nAmplificatore] = nexto
            return
        elif opcode == 5:#jump if true val[0]!= 0
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            nexto = cont + 3
            if val[0] != 0:
                nexto = val[1]            
            
        elif opcode == 6:#jump if false val[0]== 0
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            nexto = cont + 3
            if val[0] == 0:
                nexto = val[1]
        elif opcode == 7:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            if val[1] > val[0]:
                arr[arr[cont+3]] = 1
            else:
                arr[arr[cont+3]] = 0
            nexto = cont + 4
        elif opcode == 8:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            if mode2 == 0:
                val[1] = arr[arr[cont + 2]]
            else:
                val[1] = arr[cont + 2]
            if val[1] == val[0]:
                arr[arr[cont+3]] = 1
            else:
                arr[arr[cont+3]] = 0
            nexto = cont + 4
        else:
            print("problema", opcode)
            exit()
        if nexto > len(arr):
            print("interrotto")
            break
        else:
            cont = nexto
    contatori[nAmplificatore] = cont
    nastri[nAmplificatore] = arr[:]
    alt[nAmplificatore] = 1
    return (arr)


for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    stati = [i,j,k,l,m]
                    uscite = [0,0,0,0,0]
                    coso = True
                    if stati.count(0) > 1 or stati.count(1) > 1 or stati.count(2) > 1 or stati.count(3) > 1 or stati.count(4) > 1:
                        continue
                    else:
                        for n in range(5):
                            if n > 0:
                                computa(n, stati[n], uscite[n-1])
                            else:
                                computa(n, stati[n], 0)
                        if (soluzioni.count(uscite[4])) < 1:
                            soluzioni.append(uscite[4])
soluzioni.sort(reverse = True)                            
print("solution 1: ", soluzioni[0])
soluzioni = []
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    nastri = [[],[],[],[],[]]
                    for elem in temp:
                        for o in range(5):
                            nastri[o].append(elem)
                    stati = [i,j,k,l,m]
                    alt = [0,0,0,0,0]
                    contatori = [0,0,0,0,0]
                    uscite = [0,0,0,0,0]
                    coso = True
                    if stati.count(0) > 1 or stati.count(1) > 1 or stati.count(2) > 1 or stati.count(3) > 1 or stati.count(4) > 1:
                        continue
                    else:
                        while alt.count(1) < 5:
                            for n in range(5):
                                if n > 0:
                                    computaConRiserva(n, stati[n]+5, uscite[n-1])
                                else:
                                    if coso:
                                        computaConRiserva(n, stati[n]+5, 0)
                                    else:
                                        computaConRiserva(n, stati[n]+5, uscite[4])
                            coso = False
                        if (soluzioni.count(uscite[4])) < 1:
                            soluzioni.append(uscite[4])
soluzioni.sort(reverse = True)
print("solution 2: ", soluzioni[0])
