i = int (input('Enter numbers, untill 0: '))
pos = 0
neg = 0
while i != 0:
    if i > 0:
        pos = pos + 1
    else:
        neg = neg + 1
    i = int (input('Enter next number: '))
print ('Positive = ', pos, ', Negative = ', neg)
