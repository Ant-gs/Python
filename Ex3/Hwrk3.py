list1 = []
k = int(input())
for i in range (k):
    list1.append(int(input()))
for i in range (len(list1) - 1):
    for j in range (len(list1) - 1 - i):
        if list1[j] > list1[j+1]:
            list1[j] , list1[j+1] = list1[j+1] , list1[j]
print(list1)
