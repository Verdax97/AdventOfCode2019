import math
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
    
f= open("1.txt","r")
totale = 0
for x in f:
    y = int(x)
    y = y /3
    i = round_down(y)-2
    k = i/3
    m = round_down(k) -2
    if m < 0:
            m = 0
    i = i + m
    while m != 0:
        k = m/3
        m = round_down(k) -2
        if m < 0:
            m = 0
        i = i + m
    totale = totale + i
print(totale)
f.close()
