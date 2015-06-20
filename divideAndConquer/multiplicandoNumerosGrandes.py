import random
#import time

def mult(x,y):
    n = 0
    if(len(x) >= len(y)):
        ops = len(x)-len(y)
        y = ops*"0"+y[:]
        n = len(x)
    elif(len(y) >= len(x)):
        ops = len(y)-len(x) 
        x = ops*"0"+x[:]
        n = len(y)
        
    if (n == 1):        
        return int(x)*int(y)
        
    else:
        esqX = x[0:(len(x)/2)+len(x)%2]
        dirX = x[(len(x)/2)+len(x)%2:len(x)]
        esqY = y[0:(len(y)/2)+len(x)%2]
        dirY = y[(len(y)/2)+len(x)%2:len(y)]
    
    esqXesqY = mult(esqX,esqY)
    esqXdirY = mult(esqX,dirY)
    dirXesqY = mult(dirX,esqY)
    dirXdirY = mult(dirX,dirY)
    
    return esqXesqY*(10**n) + (esqXdirY + dirXesqY)*(10**(n/2)) + dirXdirY



#millis1 = int(round(time.time() * 1000))

print mult(str(111),str(24))

#mult(str(random.getrandbits(32)),str(random.getrandbits(32)))

#millis2 = int(round(time.time() * 1000))

#print millis2-millis1
