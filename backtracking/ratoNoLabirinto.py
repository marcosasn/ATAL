def ratoNoLabirinto(L, S, l, c):
	if l == (len(L)-1) and c == (len(L)-1):
		print(S)
	else:
		if l < len(L) and c < len(L[0]):
			if(valid(L,S,l,c+1)):
				S[l][c+1]=1
				ratoNoLabirinto(L, S, l, c+1)
			elif (valid(L,S,l+1,c)):
				S[l+1][c]=1
				ratoNoLabirinto(L, S, l+1, c)

def valid(L, S, i, j):
	if i < len(L) and j < len(L[0]):
		if L[i][j] == 0:
			return False
	return True


La = [[1,0,0,0], 
     [1,1,0,1],
     [0,1,0,0],
     [1,1,1,1]]


So = [[1,0,0,0], 
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

ratoNoLabirinto(La,So,0,0)



