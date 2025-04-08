all = int(input('Enter the number of videocards: '))
latest = 0
cards = []
nlistcards = []
for i in range(all):
    cards.append(int(input(f'Card {i+1} is № : ')))
    if cards[i] > latest:
        latest = cards[i]
for i in range(all):
    if cards[i] != latest:
        nlistcards.append(cards[i])
print ('Old list: ')
for i in range(all):
    print(cards[i])
print ('New list: ')
for i in range(len(nlistcards)):
    print(nlistcards[i])