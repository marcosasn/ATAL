#coding: utf-8
#The game is simple. You initially have ‘H’ amount of health and ‘A’ amount of armor. At any instant you can live in any of the three places - fire, water and air. After every unit time, you have to change your place of living. For example if you are currently living at fire, you can either step into water or air.
#If you step into air, your health increases by 3 and your armor increases by 2
#If you step into water, your health decreases by 5 and your armor decreases by 10
#If you step into fire, your health decreases by 20 and your armor increases by 5
#If your health or armor becomes <=0, you will die instantly
#Find the maximum time you can survive.

#Input:
#The first line consists of an integer t, the number of test cases. For each test case there will be two positive integers representing the initial health H and initial armor A.

#Output:
#For each test case find the maximum time you can survive.

#Note: You can choose any of the 3 places during your first move.

#Input Constraints:
#1<=t<=10
#1<=H,A<=1000 

#Example:
#Sample Input:
#3
#2 10
#4 4
#20 8

#Sample Output:
#1
#1
#5

hList= [3,-5,-20]
aList= [5,2,-10]
rules = {'fire':(-20,5),'water':(-5,-10),'air':(3,2)}

t = int(raw_input())

for i in range(t):
	h,a = map(int, raw_input().split(' '))
	time = 0
	location = (-20,5)
	
	while (h > 0 and a > 0):
		h += location[0]
		a += location[1]	
		time += 1
		
		for k in range(len(hList)):
			for j in range(len(aList)):
				if (hList[k], aList[j]) in rules.values() and (hList[k], aList[j]) != location:
					location = (hList[k], aList[j])
					break
			break	
	print time
