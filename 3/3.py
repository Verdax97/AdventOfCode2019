f = open("3.txt","r")
cavi = f.readlines()
f.close()
percorsi = []
percorsi = [cavi[0].split(","),cavi[1].split(",")]
percorsi[0][-1] = percorsi[0][-1][:-1]
w = 40000
h = 40000
origine = 0
mappa = []
for i in range(0,w):
    field = []
    for j in range(0,h):
        x = 0
        field.append(x)
    mappa.append(field)
for n in range (2):
    x = origine
    y = origine
    dist = 10000000
    #for k in range (10):
    #        print(mappa[k], k)
    #print()
    for i in range(len(percorsi[n])):
        if percorsi[n][i][0] == "U":
            a = y
            for j in range (1, int(percorsi[n][i][1:])+1, 1):
                y = a + j
                if mappa[x][y] != 0 and mappa[x][y] != n + 1 and min(dist, abs(x - origine) + abs(y - origine)) < dist:
                    dist = abs(x - origine) + abs(y - origine)
                mappa[x][y] = n + 1
        if percorsi[n][i][0] == "D":
            a = y
            for j in range (1, int(percorsi[n][i][1:])+1, 1):
                y = a - j
                if mappa[x][y] != 0 and mappa[x][y] != n + 1 and min(dist, abs(x - origine) + abs(y - origine)) < dist:
                    dist = abs(x - origine) + abs(y - origine)
                mappa[x][y] = n + 1
        if percorsi[n][i][0] == "L":
            a = x
            for j in range (1, int(percorsi[n][i][1:])+1, 1):
                x = a - j
                if mappa[x][y] != 0 and mappa[x][y] != n + 1 and min(dist, abs(x - origine) + abs(y - origine)) < dist:
                    dist = abs(x - origine) + abs(y - origine)
                mappa[x][y] = n + 1

        if percorsi[n][i][0] == "R":
            a = x
            for j in range (1, int(percorsi[n][i][1:])+1, 1):
                x = a + j
                if mappa[x][y] != 0 and mappa[x][y] != n + 1 and min(dist, abs(x - origine) + abs(y - origine)) < dist:
                    dist = abs(x - origine) + abs(y - origine)
                mappa[x][y] = n + 1
    print(dist)
