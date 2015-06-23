def exactSum(P,m, i, j,S):
    if sum(S) == m:
        return S
    else:
        mid = (i+j)/2
        S.append(P[mid])
        if P[mid] < m:
            return exactSum(P,m,i,mid,S)
        else:
            return exactSum(P,m,mid+1,j,S)

def exactSum2(P,m,i,j):
    for k in range(len(P)):
        for l in range(len(P)):
            if (P[k] <= P[l] and P[k]+P[l] == m and abs(P[k]-P[l]) <= 2):
                return (P[k],P[l])
    return (0,0)

#n = int(raw_input())
#n = 5
n=2
#P = map(int,raw_input().split())
#P = [10,2,6,8,4]
P = [40,40]
#m = int(raw_input())
#m = 10
m = 80
result = exactSum(sorted(P),m,0,len(P)-1,[])
result = sorted(result)

print "Peter should buy books whose prices are "+str(result[0])+" and "+str(result[1])+"."
