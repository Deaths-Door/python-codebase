def bubble_sort(items):
    for ix in range(len(items) -1) :
        for iy in range(len(items) -1-ix) :
            if items[iy]> items[iy+1]:
                items[iy] , items[iy+1] = items[iy+1] , items[iy]
 

items = [2,5,2,65,7,8,2]
bubble_sort(items)
print(items)
