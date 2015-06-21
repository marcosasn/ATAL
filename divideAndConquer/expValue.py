def expValue(a,n):
    if (n == 0):
        return 1
    if (n%2 == 0):
        return expValue(a,n/2) * expValue(a,n/2)
    else:
        return expValue(a,(n-1)/2) * expValue(a,(n-1)/2) * a

print expValue(2,10)
