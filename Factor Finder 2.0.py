#Factor Finder

#Check's if i is a factor
def check(num):
    return i % num == 0

#Prints factors
def form(string):
    if b == 0:
        print(string,sep='',end='')
    else:
        print(',',string,sep='',end='')

#Increases for loops
def inc(x):
    x = x + 1

#Main()
while True:
    nums = []
    primes = []
    lim = int((input("How Many #s?\n")).strip())
    for i in range(1, lim + 1):
        if i == lim:
            print(i,'-',end=' ')
        count = 0
        inc(i)
        nums.append(i)
        for b in range(0,len(nums)):
            if check(nums[b]):
                count = count + 1
                if i == lim:
                    form(nums[b])
                inc(b)
        if count == 2:
            primes.append(i)
            if i == lim:
                print(' - Prime!',end='')
        elif i == lim:
            print(' -',count,'Factors!',end='')
    print('\nThere are',len(primes),'primes between 1 and',lim,'-',primes,'\n')
