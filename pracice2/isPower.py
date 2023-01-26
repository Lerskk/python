def isPowerOfTwo(number: int) -> bool:
	if (x == 0):
		return false
	return math.log10(number) / math.log10(2)

def add(numberOne: int, numberTwo: int):
	sum = 0
	for number in range(numberOne, numberTwo + 1):
		if (isPowerOfTwo(number)):
			sum += number
	return sum

print(add(0, 7))