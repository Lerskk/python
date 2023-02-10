def score():
	sum = 0
	amount = 0
	cont = 'y'

	while cont == 'y':
		inp = int(input('score '))
		sum += inp	
		amount += 1
		cont = input('score? y/n ')

	return (sum / amount)

print(score())
