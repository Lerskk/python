def duplicated(list):
	for element in range(0, len(list)):
		for ele in range(element + 1, len(list)):
			if list[ele] == list[element]:
				return True
	return False

print(duplicated([2, 2, 3]))
print(duplicated([2, 3]))
print(duplicated([2, 9, 2]))