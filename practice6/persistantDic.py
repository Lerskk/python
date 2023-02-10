def writeData(fileName):
	dictionary = {}
	path = "/home/lerskk/code/python/practice6/" + fileName
	file = open(path)
	lines = [line.split() for line in file.readlines()]
	lines = [(line[0], line[1]) for line in lines]
	for key, value in lines:
		dictionary[key] = value
	return dictionary

print(writeData("dictionary.txt"))
	
