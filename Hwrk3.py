a = int (input("Enter number of your ticket: "))
n1 = a//100000
n2 = a%100000//10000
n3 = a%10000//1000
n4 = a%1000//100
n5 = a%100//10
n6 = a%10//1
if n1+n2+n3==n4+n5+n6:
    print ("You have a lucky ticket!")
else:
    print ("Looks like you have an ordinary ticket.")
# if a<6:
#     print ("ERROR! Ticket number must contain at least 6 digits!")
# elseif a>6 :
#     print ("ERROR! Ticket number can't contain more than 6 digits!")