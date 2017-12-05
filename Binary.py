#Binary Converter

def binToDec():
    numBin = input('Enter your Number: ')
    numDec = 0
    length = len(numBin)
    for i in range(0,length):
        if int(numBin[i]) > 1:
            print(numBin,"isn't Binary!")
        elif numBin[i] == '1':
            numDec = numDec + 2**(length - (i+1))
        i = i + 1      
    print(numDec,end='\n\n')

def decToBin():
    numDec = int(input('Enter your Number: '))
    numBin = ''
    while numDec >= 1:
        numBin = numBin + str(numDec % 2)
        numDec = numDec // 2
    print(numBin[::-1],end='\n\n')

while True:
    choice = int(input('[1] - Decimal to Binary\n[2] - Binary to Decimal\n'))
    if choice == 1:
        decToBin()
    elif choice == 2:
        binToDec()
