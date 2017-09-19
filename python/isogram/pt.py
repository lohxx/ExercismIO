def rec(n):
	if n > 0:
		return n*rec(n-1)
	else:
		return 1




def ree(n):
	l = 0
	while(n > 0):
		l += n*n
		print(n*n)
		n -= 1
	print(l)
ree(6)