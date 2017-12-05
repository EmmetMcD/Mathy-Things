#Pythagoras
import math

def form(str1,str2):
    global s1,s2
    s1 = float(input(str1))
    s2 = float(input(str2))

while True:
    choice = int(input('[1] - Pythagorean Triples\n[2] - Sin, Cos, & Tan\n'))
    if choice == 1:
        form('Side 1: ','Side 2: ')
        hyp = math.sqrt(s1**2 + s2**2)
        print('Hypotenuse:',hyp,'\n')
    elif choice == 2:
        sct = int(input('[1] - Sine\n[2] - Cosine\n[3] - Tangent\n'))
        if sct == 1:
            pyth = 'Sin'
            form('Opposite: ','Hypotenuse: ')
        elif sct == 2:
            pyth = 'Cos'
            form('Adjacent: ','Hypotenuse: ')
        elif sct == 3:
            pyth = 'Tan'
            form('Opposite: ','Adjacent: ')
        print(pyth,'(Angle): ',s1 / s2,'\n',sep='')
