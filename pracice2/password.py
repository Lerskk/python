def password():
	password = 'hi'
	max = 3
	tries = 0
	inp = ''
	correct = False
	while inp != password and tries < max:
		tries += 1
		inp = input('password: ')
		if (inp == password):
			correct = True
	return correct

print(password())