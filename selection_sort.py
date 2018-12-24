def main():
	arr = [2, 5, 7, 3, 1, 9]
	print(arr)
	arr2 = selction_sort(arr, lambda x, y : x>y)
	arr3 = selction_sort(arr, lambda x, y : x<y)
	print(arr2)
	print(arr3)


def selction_sort(A, compare=lambda x, y : x<y):
	T = A[:]
	for i in range(len(T)):
		c = i
		for j in range(i, len(T)):
			if compare(T[j], T[c]):
				c = j
		T[i], T[c] = T[c], T[i]
	return T


if __name__ == '__main__':
	main()