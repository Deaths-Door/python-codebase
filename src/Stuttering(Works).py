def stutter(string) :
    dots = string[:2] + '... '
    output = dots + dots + string + '?'
    print(output)

string = input("Enter string : ")
stutter(string)
