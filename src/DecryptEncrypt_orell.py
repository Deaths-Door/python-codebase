import re

data = {
    "A" : "7847",
    "B" : "3664",
    "C" : "8483",
    "D" : "1126",
    "E" : "8853",
    "F" : "6744",
    "G" : "0374",
    "H" : "9374",
    "I" : "8365",
    "J" : "6374",
    "K" : "1937",
    "L" : "1347",
    "M" : "8947",
    "N" : "5475",
    "O" : "6317",
    "P" : "8308",
    "Q" : "5487",
    "R" : "5267",
    "S" : "1985",
    "T" : "0747",
    "U" : "0861",
    "V" : "7678",
    "W" : "8264",
    "X" : "9936",
    "Y" : "5343",
    "Z" : "2684",
    "Ä" : "3091",
    "Ü" : "9432",
    "Ö" : "1239",
    "." : "%",
    " " : "+",
    "?" : "#",
    ":" : "/",
    "!" : "*",
    "," : "=",
}

def decrypt(s):
    for key in data: s =  s.replace(data[key],key)
    return s
def encrypt(s):
    s = s.upper()
    for key in data: s =  s.replace(key,data[key])
    return s

s = input("Enter string idiot : ")
print(decrypt(s) if(len(re.findall('[a-z|A-Z]',s)) == 0) else encrypt(s))