def dominoesPieces(n: int = 7):
	for first in range(0, n):
		for second in range(first, n):
			print([first, second])
            
dominoesPieces()
print('-----')
dominoesPieces(2)
