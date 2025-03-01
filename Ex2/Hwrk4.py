sum = 0
for m in range(1,13):
    sal = int(input(f'Enter the salary for the {m} month: '))
    sum += sal
avg = int(sum/12)
print(f'The average is {avg}')