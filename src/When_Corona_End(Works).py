import math

def end_corona(recover,new,active):
    diff = int(recover) - int(new)
    time = int(active) / int(diff)
    print(math.ceil(time))


recover,new,active = input("Enter values : ").split()
end_corona(recover,new,active)
