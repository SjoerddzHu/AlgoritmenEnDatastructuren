def machtv2(a, n):
	assert n > 0
	Counter = 0
	m = 1
	while n > 0:
		if n%2 == 0:
			a *= a
			n /= 2
			Counter += 1 
		else:
			m *= a
			n -= 1
			Counter += 1 

	print(Counter)
	return m

print(machtv2(8, 4) == 8**4)
print(machtv2(2, 7) == 2**7)
