
def main():
	arr = [2, 5, 7, 3, 1, 9]
	print(arr)
	arr2 = quick_sort(arr, lambda x, y : x>y)
	arr3 = quick_sort(arr, lambda x, y : x<y)
	print(arr2)
	print(arr3)

def get_pivot(A, low, hi):
	mid = (low+hi)//2
	pivot = hi
	if(A[low] < A[mid]):
		if(A[mid] < A[hi]):
			pivot = mid
	elif(A[low] > A[hi]):
		pivot = low
	return pivot


def split_it(A, low, hi, cp_f):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low
	for i in range(low, hi+1):
		if cp_f(A[i],pivotValue):
			border+=1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return border


def quick_sort2(A, low, hi, cp_f):
	if low < hi:
		p = split_it(A, low, hi, cp_f) #returns border index
		quick_sort2(A, low, p-1, cp_f)
		quick_sort2(A, p+1, hi, cp_f)


def quick_sort(A, compare=lambda x, y : x<y, overwrite=True):
	if overwrite:
		T = A[:]
		quick_sort2(T, 0, len(T)-1, compare)
		return T
	else:
		quick_sort2(A, 0, len(A)-1, compare)
		return A


if __name__ == '__main__':
	main()