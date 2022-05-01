from random import randrange

def enter_list():
    mylist = list((map(int, input("Enter {0} number".format(N)).split())))
    
    while True:
        if len(set(mylist)) == N:
            print("Your list is {0}".format(mylist))
            break
    
        if len(set(mylist)) !=N:
            print("You must enter unique {0} number. Enter one more time".format(N))
            mylist = list(map(int, input().split()))
    return mylist


def check_strike(List):
    strike=0; ball=0
    mylist=List
    i = 0
    
    if mylist==randomlist:
        return 99
    else:
        for m,r in zip(mylist,randomlist):
            print(m,r)
            if m==r:
                strike+=1
                mylist[i]='x'
            i+=1
            
        for m in mylist:
            print(m)
            if randomlist.count(m)!=0:
                ball+=1
        
        print("{0} strike, {1} ball".format(strike, ball))
        return -99

global N;N = int(input("Enter number 4~6 : "))
global randomlist; randomlist = []

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
global cnt; cnt=1
result = 0

while result!=99:
    mylist=enter_list()
    cnt+=1
    result=check_strike(mylist)
    
print("{0} strike! {1} times you enter".format(N, cnt))
