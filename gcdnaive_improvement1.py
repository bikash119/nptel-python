def gcd(m,n):
    gcf = 1
    for i in range(1,min(m,n)+1):
        if (m % i == 0) and (n % i == 0):
            gcf = i

    return gcf


def gcd_backward_iteration(m,n):
    gcd = 1
    for i in range(min(m,n),1,-1):
        if m % i == 0 and n % i == 0:
            gcd = i
    return gcd

def gcd_backward(m,n):
    i = min(m,n)
    while i > 0:
        if m % i == 0 and n % i == 0:
            return i
        else:
            i = i -1
#gcd(14,63)
#gcd_backward_iteration(999999,10000000)