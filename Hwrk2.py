a = int (input ("Enter the number of minutes: "))
if type(a) != int:
    print("Error! Enter NUMBER of minutes!")
else:
    print ("It's ", a//60, " hours and ", a%60, " minutes.")