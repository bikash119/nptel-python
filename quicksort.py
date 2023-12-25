import random
def rearrange(list):
    pivot = list[0]
    (orange,green) = (-1,-1)
    for i in range(0,len(list)):
        if pivot >= list[i]:
            orange += 1
            green += 1
            if green > orange:
                (list[orange],list[i]) = (list[i],list[orange])
        else:
            green = green + 1
    (list[0],list[orange]) = (list[orange],list[0])
    return list,list.index(pivot),pivot

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        (list,pivot_index,pivot) = rearrange(list)
        return quicksort(list[:pivot_index]) + [pivot] + quicksort(list[pivot_index+1:])
        

l = [43,32,22,78,63,57,91,13]
quicksort(l)