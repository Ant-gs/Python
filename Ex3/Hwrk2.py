list = ['Криминальное чтиво','Аватар','Шрек','Дикий робот']
userlist = [    ]
i = 1
question = str(input ('Hello, who are you admin or user?: '))
if question == 'admin':
    password = str(input('Enter the password: '))
    if password == 'qwe1234':
        addall = str(input('Do you want to add another movie to the list?: '))
        if addall == 'yes':
            while True:
                list.append(str(input('Enter next movie: ')))
                if list[3+i]== 'stop':
                    del list[-1]
                    break
                i += 1
elif question == 'user':
    inpu = str(input('Do you want to add some movies to the "favorite" list?: '))
    if inpu == 'yes':
        while True:
             userlist.append(str(input('Add movie: ')))
             if userlist[-1+i] == 'stop':
                 del userlist[-1]
                 break
             elif userlist[-1+i] not in list:
                print ('Sorry we have not this movie in our cinema.')
                del userlist[-1]
             else:
                 i = i + 1
for a in range (len(userlist)):
    print ('Your favorite: ')
    print (userlist[a])

