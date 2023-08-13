###########
#number of dots at the pentagon at the nth iteriation
def num_dots(n) :
	return (5 * n * n - 5 * n + 2) // 2
###########
n = int(input("Enter number : "))
print(num_dots(n))
