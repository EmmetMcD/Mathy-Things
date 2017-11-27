#Factor Finder
#Check's if i is a factor
def check(num):
    return i % num == 0
def checkAll():
    for i in range(0, len(nums)):
        check(nums[i])
        inc(i)
#Prints factors
def form(string):
    print(string,end=',')
def formAll():
    for i in range(0, len(strs)):
        form(nums[i])
        inc(i)
#increases for loops
def inc(x):
    x = x + 1
#Main()
while True:
    nums = []
    lim = int(input("How Many #s?\n"))
    for i in range(1, lim + 1):
        inc(i)
        nums.append(i)
        print(i, end=' - ')
        if checkAll():
            formAll()
        else:
            for b in range(0,len(nums)):
                if check(nums[b]):
                    form(nums[b])
                inc(b)
        print('')
        
