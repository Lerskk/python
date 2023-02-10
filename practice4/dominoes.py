def match(piceOne, piceTwo):
	if piceOne[0] == piceTwo[0] or piceOne[0] == piceTwo[1] or piceOne[1] == piceTwo[0] or piceOne[1] == piceTwo[1]:
		return True
	return False

print(match((3, 4), (5, 4)))