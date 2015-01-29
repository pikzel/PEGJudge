A = int(input())
B = int(input())
R = int(input())

if A > R:
	print('Bob overdoses on day 1.')
elif A / 2 + B > R:
	print('Bob overdoses on day 2.')
else:
	print('Bob never overdoses.')
