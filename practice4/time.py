def generateTime(hours, minutes):
	return (hours, minutes)

def addTime(timeOne, timeTwo):
	time = (timeOne[0] + timeTwo[0], timeOne[1] + timeTwo[1])
	while 60 <= time[1]:
		time = (time[0] + 1, time[1] - 60)
	return time

print(addTime(generateTime(1, 30), generateTime(1, 30)))
	