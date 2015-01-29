n = int(input())
steps = 0
while n > 1:
	if n%2 != 0: # odd
		n = n * 3 + 1
	else:
		n = n/2
	steps += 1
print(steps)