def backtracking(x,y,i):
    if x < 0 or y < 0 or x > len(matriz)-1 or y > len(matriz[0])-1:
        return False
        
    if matriz[x][y] != palavra[i]:
        return False
    
    if i == len(palavra)-1 and matriz[x][y] == palavra[i]:
        return True
    else:
        return (backtracking(x, y+1, i+1) or backtracking(x, y-1, i+1) or
         backtracking(x+1, y, i+1) or backtracking(x-1, y, i+1) or
          backtracking(x+1, y+1, i+1) or backtracking(x+1, y-1, i+1) or
           backtracking(x-1, y+1, i+1) or backtracking(x-1, y-1, i+1))
        
        
entrada = int(raw_input())
matriz = []
palavra = "allizzwell"
caminho =[]

for i in range(entrada):
    linha, coluna = map(int, raw_input().split(" "))
    
    for j in range(linha):
        matriz.append(raw_input())
        
    if backtracking(0,0,0) == True:
        print "YES"
    else: 
        print "NO"
