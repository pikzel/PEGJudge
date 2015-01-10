sum = 0
for i in range(0, int(raw_input())):
	x = int(raw_input())
	if x < 0:
		x *= -1
	sum += x
print sum