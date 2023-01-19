def add(numberOne: int, numberTwo: int):
	return numberOne + numberTwo

def sub(numberOne: int, numberTwo: int):
	return numberOne - numberTwo

def mul(numberOne: int, numberTwo: int):
	return numberOne * numberTwo

def div(numberOne: int, numberTwo: int):
	return numberOne / numberTwo

def execute(fun):
  first = int(input('first number '))
  second = int(input('second number '))

  print(fun(first, second))


def menu():
	option = int(input('''
	Select option
		1 - add
		2 - substract
		3 - multiply
		4 - divide 
		5 - exit \n'''))
	if option == 1:
		execute(add)
	if option == 2:
		execute(sub)
	if option == 3:
		execute(mul)
	if option == 4:
		execute(div)
	if option == 5:
		return
	menu()
		
menu() 