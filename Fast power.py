import random

def power(a,n):
	m = []
	while n > 0:
		m.append(n%2)
		n = n // 2
	s = 1
	q = len(m)
	for i in range(q):
		if m[q - i - 1] == 0:
			s = s*s
		else:
			s=s*s*a
	return s

a = int(input())
a = random.randint(2,10000)
n = random.randint(2,10000)
print(a,n,power(a,n),sep = '\n')
