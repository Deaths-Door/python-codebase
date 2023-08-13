import random

n = random.randint(0,100)
x = 0

while (x < 3):
    x = x + 1
    geuss = int(input("ENter number : "))
    if(geuss != n):
        print("TRY AGAIN")
    else:
        print("U geussed it")
        break