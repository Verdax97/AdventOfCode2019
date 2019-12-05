f = open("5.txt","r")
lista = f.read()
temp = lista.split(",")
f.close()
temp = list(map(int, temp))

def parte1():
    cont = 0
    nexto = cont
    arr = temp[:]
    
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
            #print(arr[cont])
            #print(opcode)
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
            valin = int(input())
            arr[arr[cont + 1]] = valin
            nexto = cont + 2
        elif opcode == 4:
            if mode1 == 0:
                val[0] = arr[arr[cont + 1]]
            else:
                val[0] = arr[cont + 1]
            print("Output: ", val[0])
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
            break
        else:
            cont = nexto
    return (arr[0])

print(parte1())