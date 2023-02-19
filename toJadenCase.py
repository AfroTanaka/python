def to_jaden_case(string):
    # ...
    stringSpl = string.split()
    
    result = []
    for i in stringSpl:
        result.append(i.capitalize())
    return " ".join(result)

string = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(string))

#return ' '.join(word.capitalize() for word in string.split())

#import string def to_jaden_case(str): return string.capwords(str)