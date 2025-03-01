import random
determinant = 0
counter = 1
mnum = random.randint(0,100)
num = int(input('Try to guess what number am i think of?(from 0 to 100): '))
while num != mnum:
    determinant = abs(mnum - num)
    num = int(input('Nope, try again): '))
    if abs(mnum - num) <= 10:
        print ('It\'s hot spot')
    elif abs(mnum - num) <= 5:
        print ('Super hot')
    if abs(mnum - num) < determinant:
        print('It\'s warmer')
    else:
        print ('It\'s colder')
    counter += 1
print ('Yes, you\'re right, congratulations!!!')
print (f"Counts: {counter}")
