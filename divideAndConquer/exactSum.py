def exactSum(P,m, i, j):
    if (i==j):
        return P[j]
    else:
        mid = (i+j)/2
        p1 = exactSum(P, m, i, mid)
        p2 = exactSum(P, m, mid+1, j)
        if (p1 <= p2 and p1+p2 == m and abs(p1-p2 <= 2)):
                return (p1,p2)
        return p2
        
def exactSum2(P,m,i,j):
    for k in range(len(P)):
        for l in range(len(P)):
            if (P[k] <= P[l] and P[k]+P[l] == m and abs(P[k]-P[l]) <= 2):
                return (P[k],P[l])
    return (0,0)


#n = int(raw_input())
n = 5
#n=2
#P = map(int,raw_input().split())
P = [10,2,6,8,4]
#P = [40,40]
#m = int(raw_input())
m = 10
#m = 80
result = exactSum(sorted(P),m,0,len(P)-1)

print "Peter should buy books whose prices are "+str(result[0])+" and "+str(result[1])+"."
