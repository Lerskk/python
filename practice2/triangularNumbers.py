def triangularNumber(number: int):
	for index in range(1, number + 1):
		triangularNumber = 0
		for subNumber in range(1, index + 1):
			triangularNumber += subNumber
		print(index, '-', triangularNumber)
        

def betterTriangularNumber(number: int):
	for index in range(1, number + 1):
		print(index, '-', (index * (index + 1)) // 2)
        
triangularNumber(5)
print('----')
betterTriangularNumber(5)