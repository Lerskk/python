def copy(file):
	target = open('cp.txt', 'w')
	for line in file:
		target.write(line)
	target.close()

f = open('/home/lerskk/code/python/practice6/head.txt')
copy(f)