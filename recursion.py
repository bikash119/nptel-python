def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

def list_len(l):
    if not l:
        return 0
    else:
        return 1 + list_len(l[1:])

def sumlist(l):
    if not l:
        return 0
    else:
        return l[0] + sumlist(l[1:])

def multiply(m,n):
    if n == 1:
        return m
    else:
        return m + multiply(m,n-1)

def insertion_sort(list):
    if len(list) == 1:
        return list
    else:
        sorted_list = insertion_sort(list[0:len(list)-1])
        sorted_list.append(list[len(list)-1])
        pos = len(sorted_list)-1
        while pos > 0 and sorted_list[pos] < sorted_list[pos-1]:
            (sorted_list[pos],sorted_list[pos-1])= (sorted_list[pos-1],sorted_list[pos])
            pos = pos - 1

        return sorted_list
insertion_sort([2,7,3,9,1,24])