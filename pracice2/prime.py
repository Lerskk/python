def prime(number):
	div = 0
	for test in range(1, number + 1):
		if (number % test == 0):
			div += 1
	return div <= 2
		

print(prime(1))
print(prime(2))
print(prime(4))
print(prime(7))