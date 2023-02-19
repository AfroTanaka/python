def nb_year(p0, percent, aug, p):
    # your code
    n = 0
    percent = percent*(1/100)
    while p0 < p:
        p0 = int(p0 + p0 * percent + aug)
        n += 1
        print('the end of', n, 'year', p0)
    return n

print(nb_year(1000, 2, 50, 1215))
