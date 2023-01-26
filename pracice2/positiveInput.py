def positiveInput():
	while True:
		inp = input('positive number: ')
		if (not(inp.isnumeric()) or int(inp) <= 0):
			print('error, invalid input')
	
positiveInput()