def get_middle(s):
    i = (len(s) -1) // 2
    return s[i:-i] or 2

print(get_middle('hello'))