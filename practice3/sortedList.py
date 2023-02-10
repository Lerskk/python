def sortedList(list):
	for element in range(1, len(list)):
		if (list[element] < list[element - 1]):
			return False
	return True

print(sortedList([1, 8, 9]))
print(sortedList([1, 9, 8]))
print(sortedList(['a', 'd', 'b']))
print(sortedList(['a', 'b', 'd']))