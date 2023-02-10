def countVowels(string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	times = [0, 0, 0, 0, 0]

	for letter in string.lower():
		if letter in vowels:
			times[vowels.index(letter)] += 1
	return times

print(countVowels('aaaa'))
print(countVowels('name'))
print(countVowels('ninny'))
print(countVowels('nnny'))