sum = 0
N = int(input('How many cards do you have?: '))
for i in range(1,N+1):
    sum += i
for i in range(N-1):
    rem = int(input("What card is remaining?: "))
    sum -= rem
print(f"Missing card is number {sum}")