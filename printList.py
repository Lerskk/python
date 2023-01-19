list = [12, 'lol', ['this', 'is', 'a', 'sublist']]
def printList(list):
	if list != []:
		print(list[0])
		printList(list[1:])

def noRecurPrintList(list):
	for element in list:
		print(element)
        
printList(list)
noRecurPrintList(list)