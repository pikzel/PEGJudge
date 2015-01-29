x = []
max = 0
for i in range(0,3):
	x.append(int(raw_input()))
for i in range(0,2):
	if x[i] > x[i+1]:
		print x[i]-x[i+1]
		break
	elif x[i] < x[i+1]:
		print x[i+1]-x[i]
		break