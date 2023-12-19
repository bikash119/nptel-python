def InsertionSort(l):
    for start in range(1,len(l)):
       pos = start
       while l[pos] < l[pos-1] and pos != 0:
           (l[pos],l[pos-1]) = (l[pos-1],l[pos])
           pos = pos -1

InsertionSort([2,7,3,9,1,24])

