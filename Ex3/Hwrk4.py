goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}
store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
}
for name in goods.keys():
   item_code = goods[name]
   total_q = 0
   total_c = 0
   for batch in store[item_code]:
      total_q += batch['quantity']
      total_c += batch['price']*batch['quantity']
   print(f'{name} - {total_q} шт., {total_c} руб.')

    