import math

def smallerDistanceBetweenTwoPoints(P,i,j):
    if (j-i<=1):
        return distance(P[i],P[j])
    midle = (i + j)/2
    dl = smallerDistanceBetweenTwoPoints(P,i,midle)
    dr = smallerDistanceBetweenTwoPoints(P,midle+1,j)
    #dc = splitDistance(P,i,j)
    #return min(min(dl,dr),dc)
    return min(dl,dr)
    
def distance(p1,p2):
	return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

P = [(3,2),(2,1),(4,5),(7,8)]
head = 0
tea = len(P)-1

print P
print smallerDistanceBetweenTwoPoints(P,head,tea)
    
