weathers = {"sunny" : "sandals",
            "rainy" : "rainboots",
            "snowy" : "snowboots"}

def footwear(i):
    print("On a " + i + "," + weathers.get(i) + " is good footwear")
    
i = input("Enter weather : ")
if( i in weathers):
    footwear(i)
else:
    print("ENTER VALID WEATHER")
