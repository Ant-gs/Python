res = ''
g = int(input('How many girls?: '))
b = int(input('How many boys?: '))
s = int(input('How many seats there are in a row?: '))
if b > g*2 or g> b*2 or g+b > s:
    print('You can\'t sit them.')
elif b >= g:
    excess = int(b-g)
    for bgb in range(excess):
        res += 'BGB'
    for bg in range(g - excess):
        res += 'BG'
else:
    excess = g - b
    for gbg in range(excess):
        res += 'GBG'
    for gb in range(b-excess):
        res += 'GB'
print(res)