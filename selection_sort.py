import matplotlib.pyplot as plt
import matplotlib
import numpy as np

N = 100
ignore = N/2
visualize = True
comparison = True



ch1 = None
counter = 0
def main():
	arr = np.arange(1, N+1, 1)
	np.random.shuffle(arr)
	if visualize:
		global ch1
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ch1 = ax.bar(np.arange(len(arr)), arr, 1, color='grey')
		plt.ion()
		plt.show()

	def updatePlt(A, i1=None, i2=None, c=None, base_sorted=False, force=False):
		global ignore, counter
		counter +=1
		if (not visualize or counter % ignore != 0) and (not force or comparison):
			return
		global ch1
		ch1.remove()
		colr = 'grey' if not base_sorted else 'green'
		ch1 = ax.bar(np.arange(len(A)), A, 1, color=colr)
		if i1:
			for i in range(i1):
				ch1[i].set_color('green')
			ch1[i1].set_color('red')
		if i2:
			ch1[i2].set_color('blue')
		if c:
			ch1[c].set_color('orange')

		#ax.set_xticks(index + bar_width / 2)

		fig.canvas.draw()

	def selction_sort(A, compare=lambda x, y : x<y):
		T = A[:]
		for i in range(len(T)):
			c = i
			for j in range(i, len(T)):
				updatePlt(T, i, j, c)
				if compare(T[j], T[c]):
					c = j
					updatePlt(T, i, j, c, force=True)
			T[i], T[c] = T[c], T[i]

		global comparison
		comparison = False
		updatePlt(T, base_sorted=True, force=True)
		comparison = True
		return T

	arr2 = selction_sort(arr)
	with matplotlib.rc_context(rc={'interactive': False}):
		plt.show()

if __name__ == '__main__':
	main()