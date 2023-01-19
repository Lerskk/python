def printEven(min = 0, generate = 1):
	for number in range(0, generate * 2, 2):
		if (min < number): 
			print(number)

printEven(25, 200)