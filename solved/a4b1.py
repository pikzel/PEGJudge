n = int(input())

inList = []

for i in range(n):
	inList.append(int(input()))
outList = sorted(inList, key=int)
for i in outList:
	print(i)