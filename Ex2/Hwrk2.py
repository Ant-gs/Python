import random
counter = 0
i = 1
shop = bool(0)
hours = 1
while hours <= 8 :
    tasks = int(input(f"How many tasks Maksim will do during {i} hour?: "))
    i += 1
    counter = counter + tasks
    rand = random.randint(0,1) 
    print (rand)
    if rand == 1:
        check = str(input('Maksim\'s wife is calling, what will he do? (type yes or no): '))
        if check == 'yes':
            shop = 1
    
    hours += 1
print ('The day is over.')
print('Maksim did ', counter , ' tasks')
if shop == 1:
    print ('Maksim should go to the shop')