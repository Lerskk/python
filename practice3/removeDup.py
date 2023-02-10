def duplicated(list, element):
	for ele in list:
		if element == ele:
			return True
	return False

def removeDup(list):
	newList = []
	for element in list:
		if not duplicated(newList, element):
			newList.append(element)
	return newList
			
def amountOfDup(list):
	return len(list) - len(removeDup(list))

list = [1, 1, 1, 1, 2]
listTwo = [1, 1, 1, 1]
listTwo = [1, 2, 3, 1]

print(removeDup(list))
print(amountOfDup(list))
print(removeDup(listTwo))
print(amountOfDup(listTwo))