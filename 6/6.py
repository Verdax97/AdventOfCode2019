def cerca(x):
    nomi = x.split(")")
    if nomi[1][-1] == "\n":
        nomi[1] = nomi[1][:-1]
    asd = dizionario.get(nomi[0])
    if asd == None:
        dizionario.update({nomi[0]: [nomi[1]]})
    else:
        dizionario[nomi[0]].append(nomi[1])

def Conta(profondita=0, temp="COM"):
    testa = dizionario.get(temp)
    if testa != None:
        for elem in testa:
            Conta(profondita+1, elem)
    dizionario["totale"] += 1 #quelli diretti
    dizionario["totale"] += profondita - 1 #quelli indiretti

def creaPercorso(nome = "YOU", temp = "COM"):
    testa = dizionario.get(temp)
    if testa != None:
        for elem in testa:#ciclo tri i figli
            if elem == nome:
                dizionario["trovato"+nome] = True
            if dizionario["trovato"+nome] == True:
                dizionario["percorso"+nome].append(temp)
                return
            creaPercorso(nome, elem)
        if dizionario["trovato"+nome] == True:
                dizionario["percorso"+nome].append(temp)

f = open("6.txt","r")

lista = f.readlines()

dizionario = dict({})

for x in lista:
    cerca(x)
f.close()

dizionario.update({"totale": 0})
dizionario.update({"trovatoYOU": False})
dizionario.update({"trovatoSAN": False})
dizionario.update({"percorsoYOU": []})
dizionario.update({"percorsoSAN": []})

Conta()

print("n orbit = ", dizionario.get("totale"))

creaPercorso()
creaPercorso("SAN","COM")

for x in range(len(dizionario.get("percorsoYOU"))):
    for y in range(len(dizionario.get("percorsoSAN"))):
        if dizionario.get("percorsoYOU")[x] == dizionario.get("percorsoSAN")[y]:
            print("n steps = ", x+y)
            exit()
