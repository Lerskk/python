def binarySearch(element, min, max, list: list):
	mid = (min + max) // 2
	print(min, max)
	if min > max:
		list.insert(min, element)
		return min + 1


	if element == list[mid]:
		return element


	if element < list[mid]:
		return binarySearch(element, min, mid - 1, list)
	return binarySearch(element, mid + 1, max, list)

list = [2, 3, 5]
print(binarySearch(9, 0, len(list) - 1, list))
print(list)