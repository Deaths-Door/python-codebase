def toF(n):
    print(1.8 * n + 32)
def toC(n):
    print((n - 32) / 1.8)
type = input("Enter to F/C:")
n = int(input("Enter number : "))
if(type == "F"):
    toF(n)
else:
    toC(n)
