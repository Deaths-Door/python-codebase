#input
n1,operator,n2 = input("Enter experession : ").split()

# + - * // ??
match operator :
    case '+':
        print(n1 + n2)
    case '-':
        print(n1 - n2)
    case '*':
        print(n1 * n2)
    case '//':
        if n2 == 0 :
            print(-1)
        else :
            print(n1 // n2)
