import numpy as np

#martix
martix = np.array([])
################
def create(n) :
    for x in range(n) :
        row = []
        for y in range(n) :
            if(x == y) :
                row.append(1)
            else :
                row.append(0)
        martix.append(row)
################
def mirror(n) :
    pass
################
def output() :
    for x in martix :
        print (' '.join(map(str,x)))
################
n = int(input("Enter size : "))
if type(n) != int :
    print("Error")
elif n > 0 :
    create(n)
else :
    mirror(abs(n))
output()
