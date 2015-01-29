n = int(raw_input())
l = []
for i in xrange(n):
	l.append(raw_input().strip())
s = l[n-1]
for i in reversed(xrange(n-1)):
	if (n+i) % 2 == 0:
		s += l[i][::-1]
	else:
		s += l[i]
print s