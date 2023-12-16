def gcd_euclid_recursion(m,n):
    if m < n:
        (m,n) = (n,m)
    if m % n == 0:
        return n
    diff = m - n
    return gcd_euclid_recursion(n,diff)

def gcd_euclid_while(m,n):
    if m < n:
        (m,n)=(n,m)
    while (m%n) != 0:
        (m,n) = (max(m-n,n),min(m-n,n))
    return n

def gcd_euclid_recursion_v2(m,n):
    if m < n:
        (m,n) = (n,m)
    if m % n == 0:
        return n
    else:
        return gcd_euclid_recursion_v2(n,m%n)
    
def gcd_euclid_recursion_while(m,n):
    if m < n:
        (m,n) = (n,m)
    while m%n != 0:
        (m,n) = (n,m%n)
    return n



