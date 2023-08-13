# password 3 + wrong lock
iPwd = input("Enter Password : ")
aPwd = "IDK"
x = 0
while(x < 2):
    if iPwd == aPwd:
        print("CRACKED")
        break
    else:
        x = x + 1
        iPwd = input("Enter Password : ")
if x == 2:
    print("LOCKED")