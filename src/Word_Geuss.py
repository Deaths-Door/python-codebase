n = "cat"
x = 0

while (x < 11):
    x = x + 1
    geuss = list(input("Enter word : "))
    if(geuss != n):
        if(geuss in n):
            print("in serect word")
        elif(n.isupper()):
            print("Your guess must be a lowercase letter!")
        else:
            print("not in serect word")
    else:
        print("U geussed it")
        break
    print("Geusses left :" + str(10-x))