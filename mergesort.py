def merge(a,b):
    a_head ,b_head = (0,0)
    c = []
    while a_head != len(a) and b_head != len(b):
        if a[a_head] < b[b_head]:
            c.append(a[a_head])
            a_head = a_head+1
        else:
            c.append(b[b_head])
            b_head = b_head +1
    if a_head == len(a):
        c.extend(b[b_head:len(b)])
    else:
        c.extend(a[a_head:len(a)])
    return c

def mergesort(list):
    if len(list) <= 1:
        return list
    else:
       a = mergesort(list[0:len(list)//2])
       b = mergesort(list[len(list)//2:len(list)])
       return merge(a,b)
    