def numSideCompute(opp):
    #doing some math for the non-x side
    global numSide
    global num1
    global num2
    num1, num2 = numSide.split(opp)

def variSideCompute(opp):
    #x-side math
    global variSide
    global intVal
    num1, num2 = variSide.split(opp)
    if 'x' in num1:
        xVal = num1
        intVal = num2
    elif 'x' in num2:
        xVal = num2
        intVal = int(num1)
    variSide = xVal

def noSpace(str):
    #removes spaces
    str.replace(" ","")

while True:
    #asking for equation & formatting
    equa = input("Provide your equation...\n")
    noSpace(equa)
    left, right = equa.split('=')
    noSpace(left)
    noSpace(right)

    #figuring out which side has x
    if 'x' in left:
        variSide = left
        numSide = right
    elif 'x' in right:
        variSide = right
        numSide = left
    print("x is in",variSide)
    
    #compute numSide
    if '+' in numSide:
        numSideCompute('+')
        numSide = int(num1) + int(num2)
    elif '-' in numSide:
        numSideCompute('-')
        numSide = int(num1) - int(num2)
    elif '*' in numSide:
        numSideCompute('*')
        numSide = int(num1) * int(num2)
    elif '/' in numSide:
        numSideCompute('/')
        numSide = int(num1) / int(num2)

    #computing the x side
    if '+' in variSide:
        variSideCompute('+')
        numSide = int(numSide) - int(intVal)
    elif '-' in variSide:
        variSideCompute('-')
        numSide = int(numSide) + int(intVal)
    elif '*' in variSide:
        variSideCompute('*')
        numSide = int(numSide) / int(intVal)
    elif '/' in variSide:
        variSideCompute('/')
        numSide = int(numSide) * int(intVal)

    #reads out answer
    print(variSide,"=",numSide)
