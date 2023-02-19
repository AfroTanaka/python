def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk)!=10:
        return False
    n = 0
    s = 0
    w = 0
    e = 0
    for i in walk:
        if i == "n":
            n+=1
        elif i == "s":
            s+=1
        elif i == "w":
            w+=1
        elif i == "e":
            e+=1
    return n == s and w == e

print(is_valid_walk(['N','n','e','e','s','s','w','w']))