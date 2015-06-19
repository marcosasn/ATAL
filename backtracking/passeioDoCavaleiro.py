def passeioDoCavaleiro(T, i, l, c):
	if i == sum(T[0]):
		print T
	else:
		if l >= 0 and l < len(T) and c >= 0 and c < len(T[0]):
			if valid(T,i+1, l-2, c-1):
				T[l-2][c-1] = i+1
				passeioDoCavaleiro(T, i+1, l-2,c-1)
			elif valid(T,i+1, l-2, c+1):
				T[l-2][c+1] = i+1
				passeioDoCavaleiro(T, i+1, l-2,c+1)
			elif valid(T,i+1, l-1, c-2):
				T[l-1][c-2] = i+1
				passeioDoCavaleiro(T, i+1, l-1,c-2)
			elif valid(T,i+1, l-1, c+2):
				T[l-1][c+2] = i+1
				passeioDoCavaleiro(T, i+1, l-1,c+2)
			elif valid(T,i+1, l+1, c-2):
				T[l+1][c-2] = i+1
				passeioDoCavaleiro(T, i+1, l+1,c-2)
			elif valid(T,i+1, l+1, c-2):
				T[l+1][c-2] = i+1
				passeioDoCavaleiro(T, i+1, l+1,c-2)
			elif valid(T,i+1, l+2, c-1):
				T[l+2][c-1] = i+1
				passeioDoCavaleiro(T, i+1, l+2,c-1)
			elif valid(T,i+1,l+2, c+1):
				T[l+2][c+1] = i+1
				passeioDoCavaleiro(T, i+1, l+2,c+1)	

def valid(T,i,l,c):
	if l >= 0 and l < len(T) and c >= 0 and c < len(T[0]):
		if T[l][c] == 0 and l+c != 0:
			return True
	return False



Tab = [[0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]]
      

passeioDoCavaleiro(Tab,0,0,0)

for i in range(len(Tab)):
	print Tab[i]
