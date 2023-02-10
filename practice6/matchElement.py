def timesItMatch(element, list):
	matches = 0
	for elem in list:
		if elem == element:
			matches += 1
	return matches

def indexOfMatch(element, list):
	list.index(element)

def listOfIndex(element, list):
	matches = []
	for iElem in range(len(list)):
		if list[iElem] == element:
			matches.append(iElem)
	return matches

def awful(element, list, matches):
	try:
		matches.append(indexOfMatch(element, list) + len(matches))
		awful(element, list[1:])
	except:
		return matches


print(listOfIndex(1, [1, 1, 1, 2, 1]))
print(awful(1, [1, 1, 1, 2, 1], []))
