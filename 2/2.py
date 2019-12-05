f = open("2.txt","r")
lista = f.read()
temp = lista.split(",")
f.close()
temp = list(map(int, temp))

def parte1(x=12, y=2):
    cont = 0
    arr = temp[:]
    arr[1] = x
    arr[2] = y
    while arr[cont] != 99:
        if arr[cont] == 1:
            arr[arr[cont + 3]] = arr[arr[cont + 1]] + arr[arr[cont + 2]]
        elif arr[cont] == 2:
            arr[arr[cont + 3]] = arr[arr[cont + 1]] * arr[arr[cont + 2]]
        else:
            print("problema")
        if cont + 4 > len(arr):
            break
        else:
            cont += 4
    return (arr[0])
def parte2():
    for x in range(100):
        for y in range(100):
            if  parte1(x,y)== 19690720:
                return 100 * x + y

print(parte1())
print(parte2())
