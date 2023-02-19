def is_isogram(string):
    #your code here
    stringLst = list(string.upper())
    print(stringLst)
    for i in stringLst:
        print(i)
        stringLst.remove(i)
        print(stringLst)
        print(i)
        if i in stringLst:
            return False
    return True

print(is_isogram("ODGNMNqFyTWvKt"))