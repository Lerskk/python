def addFifty(number = 50, summ = 0):
	if (number < 0):
		print(summ)
		return
	addFifty(number - 1, summ + number)


addFifty(5)