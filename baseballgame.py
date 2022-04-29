from random import randrange

N = int(input("Enter number 4~6 : "))
randomlist = []
if N < 7:
    for i in range(N):
        number = randrange(10)
        while number in randomlist:
            number = randrange(10)
        randomlist.append(number)
else:
    print("N is too big!! You should enter 4~6")
    exit()

print(randomlist)

mylist = list(map(int, input("Enter {0} number".format(N)).split()))

while len(mylist) != N:
    print("You must enter {0} number. Enter one more time".format(N))
    mylist = list(map(int, input().split()))
    
print(mylist)