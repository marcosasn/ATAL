def mergeSort(A, left, right):
    if (left < right):
        midle = (left + right)/2
        mergeSort(A,left,midle)
        mergeSort(A, midle+1, right)
        return intercala(A,left,right,midle)
        
def intercala(A,left,right,midle):    
    i = left
    j = right
    result =[0]*len(A)
    
    while (i <= midle):
         result[i] = A[i];
         i+=1
    
    k = midle+1
    while(k <= right):
        result[right+midle+1-k] = A[k];
        k+=1
    
    j=right
    k=i=left 
    while(k<=right):
        if (result[i] <= result[j]):
            A[k] = result[i];
            i+=1;
        else:
            A[k] = result[j];
            j-=1;
        k+=1
    return A;
        
A = [3,2,1,5]
head = 0
tea = len(A)-1

print A
print mergeSort(A, head, tea)
