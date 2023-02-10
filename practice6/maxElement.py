def maxElement(list):
	if list != []:
		max = (list[0], 0)
	else:
		max = None

	for element in list:
		if max[0] < element:
			max = (element, list.index(element))
	return max

print(maxElement([9, 2, 8, 6]))
print(maxElement([9, 2, 9, 6]))
print(maxElement([6, 2, 9, 6]))
print(maxElement(['a', 'b', 'd', 'c']))
print(maxElement([]))