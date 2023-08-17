# money --  + interest -- total balance -- withdraw + 20%

balance = int(input("Enter Balance : "))
month = 1
loan = 0

while(month <= 12):
    withdraw = int(input("Enter Withdraw, enter NO for no withdraw : "))

    if withdraw != "NO":
        if withdraw > balance:
            balance -= withdraw
            loan = abs(balance) + abs(balance) * 0.2
            
        else:
            balance -= withdraw
    else:
        continue
        #interest monthly
    if balance > 1:
         balance += balance * 0.1
    elif balance < 1:
        balance = balance + (abs(balance) * 0.1)
    print("Balance : ",balance)
    print("Loan : ",loan)        