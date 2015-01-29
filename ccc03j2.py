import math


def print_rect(n):
	w = h = 0
	#w, h = find_factors_with_smallest_perimeter(get_all_factors(n))
	w, h = get_smallest_factors(n)
	p = w * 2 + h * 2
	print('Minimum perimeter is', p, 'with dimensions', w, 'x', h)


def get_all_factors(n):
	factors = []
	for i in range(2, int(n / 2 + 1)):
		for j in range(int(n / 2 + 1), 2, -1):
			if i > j: break  # Loes det haer med for-villkoret istaellet
			if i * j == n:
				factors.append((i,j))
	return factors
	
def get_smallest_factors(n):
	f1 = f2 = 0
	for i in range(2, int(n / 2 + 1)):
		for j in range(int(n / 2 + 1), 2, -1):
			if i > j: break
			if i * j == n:
				if i-j < f1-f2 or f1 == 0:
					f1 = i
					f2 = j
	return f1, f2

def find_factors_with_smallest_perimeter(factors):
	f1 = f2 = 0
	for f in factors:
		i,j = f
		if i*2 + j*2 < f1*2+f2*2 or f1 == 0:
			f1 = i
			f2 = j
	return f1,f2

nums = []
while True:
	C = int(input())
	if C == 0: break
	nums.append(C)
for num in nums:
	print_rect(num)