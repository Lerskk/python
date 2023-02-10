def interest(amountOfMoney: float, interestRate: float, amountOfYears: int):
	return amountOfMoney * (1 + interestRate / 100) ** amountOfYears

print(interest(100, 0.2, 1))