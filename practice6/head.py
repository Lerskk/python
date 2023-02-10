def head(file, number):
	lines = file.readlines()
	count = 0
	for line in lines:
		count += 1
		if number < count:
			break
		print("Line {}: {}".format(count, line))

f = open('/home/lerskk/code/python/practice6/head.txt')
head(f, 2)