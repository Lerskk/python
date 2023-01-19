def iterativeFactorial(n):
	factorial = 1
	for number in range(1, n + 1):
		factorial = factorial * number
	print(factorial)
		
iterativeFactorial(5)
iterativeFactorial(-5)