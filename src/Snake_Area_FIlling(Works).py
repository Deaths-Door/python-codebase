'''
n * n grid
if snake eats, its length doubles
number of times snake can eat b4 grid filled
'''



def times(n) :
    x = 0
    length = 1
    while length <= n :
        n = n - length
        x += 1
        length *= 2
    print(x)

n = input("Enter size : ")
n = int(n) * int(n)
times(n)
