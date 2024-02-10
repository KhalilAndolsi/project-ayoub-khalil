def numImpair(n):
    r = ""
    d = 2
    while r == "" and d < n:
        if n % d != 0:
            r = str(d)
        d += 1
    return r

def lesChifre(n):
    r = ""
    for i in range(len(str(n))):
        r += str(n)[i] + ", "
    return r[:-2]
    
def valideNums(n):
    valide = True
    i = 0
    while valide and i < len(str(n)):
        valide = ((int(str(n)[i])%2) == 0)
        i += 1
    return valide

