def moreAndLess(min: int, max: int):
	if (min == max):
		return min
	return min + moreAndLess(min + 1, max)
			
print(moreAndLess(2, 5))