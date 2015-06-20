import random
#import time

def mult(a,b):
    n = 0
    if(len(a) >= len(b)):
        ops = len(a)-len(b)
        b = ops*"0"+b[:]
        n = len(a)
    elif(len(b) >= len(a)):
        ops = len(b)-len(a) 
        a = ops*"0"+a[:]
        n = len(b)
        
    if (n == 1):        
        return int(a)*int(b)
        
    else:
        ae = a[0:(len(a)+1)/2]
        ad = a[(len(a)+1)/2:len(a)]
        be = b[0:(len(b)+1)/2]
        bd = b[(len(b)+1)/2:len(b)]
    
    x1 = mult(ae,be)
    x2 = mult(ae,bd)
    x3 = mult(str(int(ae)+int(ad)),str(int(be)+int(bd)))
    
    return x1*(10**n) + (x3-x1-x2)*(10**(n/2)) + x2

#millis1 = int(round(time.time() * 1000))

print mult(str(11),str(24))

#mult(str(random.getrandbits(32)),str(random.getrandbits(32)))

#millis2 = int(round(time.time() * 1000))

#print millis2-millis1
