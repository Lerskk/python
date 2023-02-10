def monthLength(year):
	lengths = [(31, 'January'), (31, 'March'), (30, 'April'), (31, 'May'), (30, 'June'), (31, 'July'), (31, 'August'), (30, 'September'), (31, 'October'), (31, 'November'), (31, 'December')]
	if year % 4 == 0:
		lengths.insert(1, (29, 'February'))
		return lengths
	lengths.insert(1, (28, 'February'))
	return lengths

def getMonthLength(month, year):
	for mon in monthLength(year):
		if mon[1] == month:
			return mon[0]
		

def nextMonth(month):
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	if month == 'December':
		return 'January'
	return months[months.index(month) + 1]

def nextDay(day_month_year):
	(day, month, year) = day_month_year
	if day >= getMonthLength(month, year):
		if month == 'December':
			return (1, 'January', year + 1)
		return (1, nextMonth(month), year)
	return (day + 1, month, year)

print(nextDay((28, 'February', 2004)))
print(nextDay((29, 'February', 2004)))
print(nextDay((31, 'December', 2004)))
print(nextDay((32, 'August', 2004)))
print(nextDay((32, 'December', 2004)))