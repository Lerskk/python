def binarySearch(element, list):
	if (element == list[len(list) // 2]):
		return True
	if len(list) == 1:
		return False
	if (element < list[len(list) // 2]):
		return binarySearch(element, list[0 : len(list) // 2])
	return binarySearch(element, list[len(list) // 2 : len(list)])

print(binarySearch('a', ['a']))
print(binarySearch('a', ['a', 'b', 'c', 'd']))
print(binarySearch('c', ['a', 'b', 'c', 'd']))
print(binarySearch('c', ['a', 'b', 'd']))
print(binarySearch('z', ['a', 'b', 'd']))
print(binarySearch('h', ['a', 'b', 'c', 'd', 'p']))