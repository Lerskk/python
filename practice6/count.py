def count(file):
	amountOfLines = len(f.readlines())
	f.seek(0)
	amountOfWords = len(file.read().split())
	f.seek(0)
	amountOfCharacters = len(file.read())

	return (amountOfLines, amountOfWords, amountOfCharacters)


f = open('/home/lerskk/code/python/practice6/head.txt')
print(count(f))