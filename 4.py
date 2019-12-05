inizio = 138307
fine = 654505
i = inizio
contatore = 0
while i < fine:
    t = str(i)
    coppia = False
    coppola = False
    crescente = True
    stato = [0,0,0,0,0,0,0,0,0,0]
    for j in range(len(t)-1):
        if int(t[j]) > int(t[j+1]):
            crescente = False
        stato[int(t[j])] += 1
        if t.count(t[j]) == 2:
            coppia = True
    if t.count(t[5]) == 2:
            coppia = True
    for j in range(10):
        if stato[j] == 2:
            coppola = True
    if crescente and coppia:
        contatore = contatore + 1
    i = i + 1
print(contatore)