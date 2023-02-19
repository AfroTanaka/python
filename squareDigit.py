def square_digits(num):
    numStr = str(num)
    result = [int(i) for i in numStr]
    #for i in numStr:
    #    result.append(int(i))
    
    return int("".join([str(x*x) for x in result]))

print(square_digits(9191))