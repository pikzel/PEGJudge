pB = map(int, raw_input().split(' ')) #Builder position
pW = map(int, raw_input().split(' ')) #Wallls coordinates

if pB[0] > pW[0] and pB[0] < pW[2] and pB[1] >  pW[1] and pB[1] < pW[3]:
	print 'Yes'
else:
	print 'No'