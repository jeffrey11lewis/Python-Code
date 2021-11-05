def CombinationRepetitionUtil(chosen, arr, index,
							r, start, end):
	iterations = 1					
	if index == r:
                for j in range(r):
                    
                    print(chosen[j], end = " ")
                print()
                return
        
	if start > n:
		return

	chosen[index] = arr[start]

	CombinationRepetitionUtil(chosen, arr, index + 1,
							r, start, end)
	CombinationRepetitionUtil(chosen, arr, index,
							r, start + 1, end)


def CombinationRepetition(arr, n, r):
	chosen = [0] * r

	CombinationRepetitionUtil(chosen, arr, 0, r, 0, n)

arr = [ 'Julia', 'Lucas', 'Mia' ]
r = 3
n = len(arr) - 1

CombinationRepetition(arr, n, r)

# This code is contributed by Vaibhav Kumar 12.
