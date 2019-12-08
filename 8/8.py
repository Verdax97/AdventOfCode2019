f = open("8.txt","r")
lista = f.read()
f.close()
w = 25
h = 6
layers = []
zeri = []
uni = []
due = []
for i in range(0, len(lista), w*h):
    layers.append(lista[i:i+w*h])
for layer in layers:
    temp = 0
    asd = 0
    coso = 0
    for j in range(w*h):
        if int(layer[j]) == 0:
            temp += 1
        if int(layer[j]) == 1:
            asd += 1
        if int(layer[j]) == 2:
            coso += 1
    zeri.append(temp)
    uni.append(asd)
    due.append(coso)
minimo = 0
for i in range(len(zeri)):
    if zeri[i] < zeri[minimo]:
        minimo = i
print("solution 1:", uni[minimo] * due[minimo])
final = []
for i in range(len(layers[0])):
    pixel = int(layers[0][i]) #2 trasparente, 1 bianco, 0 nero
    profondita = 0
    while pixel == 2:
        profondita += 1
        pixel = int(layers[profondita][i])
    final.append(pixel)
print("solution 2:")
uni[0] = 0
due[0] = 0
for i in range(h):
    for j in range(i*w, i*w + w):
        print(final[j], end="")
    print()
