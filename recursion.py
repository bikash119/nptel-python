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