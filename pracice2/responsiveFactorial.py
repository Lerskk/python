def factorial(number: int):
	factorial = 1
	for index in range(1, number + 1):
		factorial = factorial * index 
	return factorial

def responsiveFactorial(amountOfNumbers: int):
	for index in range(0, amountOfNumbers):
		number = int(input('number to calculate '))
		print(factorial(number))

amountOfNumbers = int(input('how many numbers do you want to calculate '))	

responsiveFactorial(amountOfNumbers)