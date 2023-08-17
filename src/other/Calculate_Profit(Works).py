def calc(sales):
    revenue = float(sales[2]) *  float(sales[3])
    pc = float(sales[1]) * float(sales[3])
    print(round(revenue - pc))

'''
Cost  = 1
Price = 2
Inventory = 3
'''
#input in dictionary
sales = {1 : 0, 2 : 0,3 : 0}
for x in range(1,4) :
    sales[x] = input("Enter value : ")
#calc profit
calc(sales)
