#coding: utf-8

def buscaBinariaNumero42(L, head, tea):
	if (head == tea):
		return -1
		
	meio = (head+tea)/2
	if (42 == L[meio]):
		return meio
	else:           
		if (42 < L[meio]):
			return buscaBinariaNumero42(L, head, meio)
		else:
			return buscaBinariaNumero42(L, meio+1, tea)
			

#L = map(int, raw_input().split())

conteins = [1,3,4,6,8,9,11,42,43]
nconteins = [1,3,4,6,8,9,11]

head = 0
tea = len(conteins)-1
tea2 = len(nconteins)

print buscaBinariaNumero42(conteins,0,tea)
print buscaBinariaNumero42(conteins,0,0)  
print buscaBinariaNumero42(nconteins,0,tea2)  
    
