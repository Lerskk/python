def filterFive(string):
	words = []
	for word in string.split(' '):
		if len(word) < 5:
			words.append(word)
	return ' '.join(words)
		
print(filterFive('lol this is looooong'))
