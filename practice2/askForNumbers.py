def askForNumbers():
	first = int(input('first '))
	second = int(input('second '))
    
	while (first < second):
		print([first, second])
		second = int(input('second '))
	return

askForNumbers()