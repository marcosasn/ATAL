def soma(A,i,j):
    if (i == j):
        return A[j]
    midle = (i + j)/2
    return soma(A, i, midle) + soma(A,midle+1,j)
    
A = [3,2,1,5]
head = 0
tea = len(A)-1

print A
print soma(A, head, tea)
    
    
