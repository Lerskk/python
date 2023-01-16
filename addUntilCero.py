def addInput():
	number = int(input('number '))
	if number == 0:
		return 0
	return number + addInput()

print(addInput())