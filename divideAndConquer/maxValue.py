def maxValue(A,i,j):
    if (i == j):
        return A[j]
    midle = (i + j)/2
    v1 = maxValue(A, i, midle)
    v2 = maxValue(A,midle+1,j)
    return max(v1,v2)
        
    
A = [3,2,1,5]
head = 0
tea = len(A)-1

print A
print maxValue(A, head, tea)
    
    
