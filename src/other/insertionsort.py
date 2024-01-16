def insertion_sort(items):
    key , y = 0 , 0 
    for x,item in enumerate(items) :
        key = item
        y=x-1
        while y>=0 and items[y]>key:
            items[y+1]=items[y]
            y-=1
        items[y+1]=key
 

items = [2,5,2,65,7,8,2]
insertion_sort(items)
print(items)
