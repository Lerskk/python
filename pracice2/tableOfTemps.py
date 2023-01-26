def farToCel(number: int):
	return (number - 32) * 5 / 9

def tableOfTemps():
	for temp in range(0, 130, 10):
		print(temp, ' ', farToCel(temp))
        
tableOfTemps()