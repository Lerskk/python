def countWords(phrase):
	dic = {}
	keys = []
	phrase = phrase.split(' ')
	for word in phrase:
		if word in dic:
			dic[word] = dic[word] + 1
		else:
			dic[word] = 1
			keys.append(word)
	return dic

print(countWords('a beautiful day in the beautiful town'))