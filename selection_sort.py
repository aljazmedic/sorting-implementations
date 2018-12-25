import matplotlib.pyplot as plt
import numpy as np


N = 100
ch1 = None
visualize = True
counter = 0
ignore = N/2

def main():
	arr = np.arange(1, N, 1)
	np.random.shuffle(arr)
	if visualize:
		global ch1
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ch1 = ax.bar(np.arange(len(arr)), arr, 1, color='grey')
		plt.ion()
		plt.show()

	def updatePlt(A, i1, i2):
		global ignore, counter
		counter +=1
		if not visualize or counter % ignore != 0:
			return
		global ch1
		ch1.remove()
		ch1 = ax.bar(np.arange(len(A)), A, 1, color='grey')
		ch1[i1].set_color('r')
		ch1[i2].set_color('b')
		#ax.set_xticks(index + bar_width / 2)

		fig.canvas.draw()

	def selction_sort(A, compare=lambda x, y : x<y):
		T = A[:]
		for i in range(len(T)):
			c = i
			for j in range(i, len(T)):
				updatePlt(T, i, j)
				if compare(T[j], T[c]):
					c = j
			T[i], T[c] = T[c], T[i]
		return T

	arr2 = selction_sort(arr, lambda x, y : x>y)

	


if __name__ == '__main__':
	main()