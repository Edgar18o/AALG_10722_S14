def caminosFB(lab, f, c):
    global op
    op += 1
    if f == len(lab)-1 and c == len(lab[0])-1:
        if lab[f][c] == 1:
            return 1
        else:
            return 0
    elif c == len(lab[0])-1:
        if lab[f][c] == 1:
            return caminosFB(lab, f+1, c)
        else:
            return 0
    elif f == len(lab)-1:
        if lab[f][c] == 1:
            return caminosFB(lab, f, c+1)
        else:
            return 0
    else:
        if lab[f][c] == 1:
            return caminosFB(lab, f, c+1) + caminosFB(lab, f+1, c)
        else:
            return 0
    
lab = [
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,0,1,1,0,1,1],
    [1,1,0,1,1,1,1,1],
    [1,1,1,0,0,1,0,1],
    [1,0,1,1,1,0,1,1],
    [1,1,1,1,1,1,1,1]
]

op = 0
res = caminosFB(lab, 0, 0)
print(f"En FB hay {res} caminos (ops:{op})")
