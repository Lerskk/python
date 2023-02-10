def grep(expression, file):
	lines = file.readlines()
	file.seek(0)
	lines = [line.split() for line in lines]
	for lineNumber in range(len(lines)):
		for word in lines[lineNumber]:
			if expression == word:
				return lineNumber
	file.seek(0)
	return -1
		
file = open("/home/lerskk/code/python/practice6/cp.txt")
print(grep("hi", file))
print(grep("im", file))
print(grep("i'm", file))
print(grep("modified", file))