def descending_order(num):
    # Bust a move right here
    """numStr = str(num)
    numL = []
    
    for i in numStr:
        numL.append(i)
    
    numSorted = sorted(numL, reverse=True)
    numResult = int("".join(map(str, numSorted))) # numSorted: str list -> numSorted: str strings
    
    return numResult"""
    # return int("".join(sorted(str(num(, reverse=True)))))
    return int("".join(sorted(str(num), reverse=True)))

print(descending_order(42145))