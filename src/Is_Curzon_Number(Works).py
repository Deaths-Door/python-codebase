def is_curzon(num):
    a = 2 ** int(num) + 1
    b = 2 * int(num) + 1
    if a %b == 0:
        print("True")
    else:
        print("False")

num = input("Enter number : ")
is_curzon(num)
