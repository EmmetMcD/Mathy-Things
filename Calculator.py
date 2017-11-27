#Defining possible inputs
add = set(["add", "plus", "addition", "+", "&", "sum"])
sub = set(["subtract", "minus", "takeway", "subtraction", "-", "_"])
multi = set(["multiply", "times", "x", "product", "multiplication", "*"])
div = set(["divide", "division", "fraction"])

#Checking user input
effect = input("What would you like to do?\n")
if effect.lower() in add:
    op = 0 
elif effect.lower() in sub:
    op = 1
elif effect.lower() in multi:
    op = 2
elif effect.lower() in div:
    op = 3
else:
    print(effect, "Isn't a thing, sorry!")
    
#Getting #s
num1 = int(input("What is the first number?\n"))
num2 = int(input("What is the second number?\n"))

#Doing the math
if op == 0:
    print(num1, "+", num2, "=", num1 + num2)
elif op == 1:
    print(num1, "-", num2, "=", num1 - num2)
elif op == 2:
    print(num1, "x", num2, "=", num1 * num2)
elif op == 3:
    print(num1, "÷", num2, "=", num1 / num2)
