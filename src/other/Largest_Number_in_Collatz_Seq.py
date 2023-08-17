############
def collatz_seq(n) :
    largest = n
    while n != 1 :
        #even
        if n %2 == 0 : n = n /2
        else : n = n * 3 + 1
        largest = max(largest,n)
    return int(largest)
############
n = int(input("Enter number : "))
print(collatz_seq(n))
