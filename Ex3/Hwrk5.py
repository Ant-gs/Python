all_orders = int(input('Enter quantity of orders'))
database = dict()
for i_order in range(all_orders):
    customer, pizza, count = input('{} order: '.format(i_order+1)).split() 
    count = int(count)
    if customer not in database:
        database[customer] = {pizza:count}
    else:
        if pizza in database[customer]:
            database[customer][pizza] += count
        else:
            database[customer][pizza] = count
for customer in sorted(database.keys()):
    print (f'{customer}: ')
    for pizza in sorted(database[customer].keys()):
        print(f' {pizza}: {database[customer][pizza]}')
