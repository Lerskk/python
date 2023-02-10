def countLetters(letter, string):
	times = 0
	for currentLetter in string:
		if currentLetter == letter:
			times += 1
	return times

print(countLetters('l', 'hello'))
print(countLetters('z', 'hello'))