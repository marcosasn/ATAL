#coding: utf-8

def buscaBinaria(L, head, tea, x):
	if (head == tea):
		return tea
		
	meio = (head+tea)/2
	if (x == L[meio]):
		return meio
	else:           
		if (x < L[meio]):
			return buscaBinaria(L, head, meio, x)
		else:
			return buscaBinaria(L, meio+1, tea, x)
			

A = [1,3,4,6,8,9,11]
head = 0
tea = len(A)-1

print buscaBinaria(A,0,tea,4)
print buscaBinaria(A,0,0,4)  
print buscaBinaria(A,0,tea,1) 
print buscaBinaria(A,0,tea,11)  
    
