def count_smileys(arr):
    if [x for x in arr if x not in [":",";","-","~",")","D"]]:
        return False

print(count_smileys(':}'))