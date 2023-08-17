####################
#vowels
vowels = {
    'a' : '0',
    'e' : '1',
    'i' : '2',
    'o' : '3',
    'u' : '4'
 }
####################
def encrypt(s1) :
    #reverse string
    s1 = s1[::-1]
    #replace vowels
    for x in vowels:
      s1 = s1.replace(x,vowels[x])
    s1 += 'aca'
    return s1
####################
s1 = input("Enter string : ")
print(encrypt(s1))


'''
Another way
def encrypt(word):
	return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'
'''
