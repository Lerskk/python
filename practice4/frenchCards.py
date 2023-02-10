import random

def makeSuit(suit):
	if suit == 0:
		return "hearts"
	if suit == 1:
		return "diamonds"
	if suit == 2:
		return "clubs"
	return "spades"

def makeCard(number, suit):
	if (1 < number and number <= 10):
		return (number, makeSuit(suit))
	if number == 1:
		return ("ace", makeSuit(suit))

	if number == 11:
		return ("Jack", makeSuit(suit))

	if number == 12:
		return ("Queen", makeSuit(suit))

	return ("King", makeSuit(suit))


def generateDeck():
	deck = []
	for suit in range (0, 4):
		for number in range(1, 14):
			deck.append(makeCard(number, suit))
	return deck

def drawCard(deck):
	card = deck[random.randint(0,len(deck))]
	deck.remove(card) 
	return card

def drawHand():
	deck = generateDeck()
	hand = []
	for i in range(0, 5):
		hand.append(drawCard(deck))
	return(hand)


def poker():
	hand = drawHand()
	handNumbers = [number for (number, _) in hand]
	for iNumber in range(6):
		for iCompare in range(iNumber, 6):
			
			


	print(handNumbers)


poker()