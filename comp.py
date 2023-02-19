def comp(array1, array2):
    # your code
    if array1 == [] or array2 == []:
        return False
        
    for i in array2:
        if i in array1:
            array1.remove(i)
            
    for v in array2:
        vSqrt = int(v**0.5)
        if vSqrt in array1:
            array1.remove(vSqrt)
            print(vSqrt)
        else:
            return False
    
    return False if array1 else True


# Copy
def comp(array1, array2):
    # your code
    if array1 == [] and array2 == []:
        return True
    
    
    if array1 == [] or array2 == []:
        return False
    
    if len(array1) != len(array2):
        return False
            
    for v in array2:
        vSqrt = v**0.5
        if vSqrt in array1:
            array1.remove(vSqrt)
        else:
            return False
    
    return not array1

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1, a2))