def cipher(origin, destination):
	lines = [line.split() for line in origin.readlines()]
	for line in lines:
		for word in line:
			cipheredWord = ""
			for letter in word:
				cipheredWord += chr((ord(letter) + 13) % 26)
			destination.write(cipheredWord)
			

origin = open("/home/lerskk/code/python/practice6/cp.txt")
destination = open("/home/lerskk/code/python/practice6/cipheredFile.txt", "+w")
			
cipher(origin, destination)

origin.close()
destination.close()