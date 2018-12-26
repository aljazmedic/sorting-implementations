import matplotlib.pyplot as plt
import matplotlib
import numpy as np

N = 100
ignore = N/2
visualize = True



ch1 = None
counter = 0
def main():

	def updatePlt(A, end, base_sorted=False, force=False):
		global ignore, counter
		counter +=1
		if (not visualize or counter % ignore != 0) and not force:
			return
		global ch1
		ch1.remove()
		colr = 'grey' if not base_sorted else 'green'
		ch1 = ax.bar(np.arange(len(A)-1), A[1:], 1, color=colr)
		for i in range(end):
			ch1[i].set_color('SkyBlue')
		#ax.set_xticks(index + bar_width / 2)

		fig.canvas.draw()

	class Heap:
		def __init__(self, l=[], comparator=lambda x, y : x<y):
			self.array = [0]
			self.length = 0
			self.compare = comparator
			for i, e in enumerate(l):
				updatePlt(self.array + list(l[i:]), self.length)
				self.enque(e)
			if sort:
				self.sort()

		def enque(self, a):
			self.array.append(a)
			self.length += 1
			self.__upcheck(self.length)

		def deque(self):
			self.__swap(1, self.length) #first and last
			ret = self.array.pop()
			self.length -= 1
			self.__downcheck(1)
			return ret

		def __swap(self, a,b):
			if a==0 or b==0 or a == b:
				return
			self.array[b], self.array[a] = self.array[a], self.array[b]

		def __upcheck(self, index):
			parent = index//2
			#updatePlt(self.array, self.length)
			if self.compare(self.array[parent], self.array[index]) and index > 1:
				self.__swap(index, parent)
				self.__upcheck(parent)

		def __downcheck(self, index):
			left = 2*index
			right = 2*index+1
			largest = index
			#updatePlt(self.array, self.length)
			if left <= self.length and self.compare(self.array[largest], self.array[left]):
				largest = left
			if right <= self.length and self.compare(self.array[largest], self.array[right]):
				largest = right
			if index != largest:
				self.__swap(largest, index)
				self.__downcheck(largest)

		def sort2(self):
			self.__swap(1, self.length) #first and last
			self.length -= 1
			self.__downcheck(1)

		def sort(self):
			while(self.length > 0):
				self.sort2()
				updatePlt(self.array, self.length, True)
			updatePlt(self.array, self.length, True, force=True)

		def __str__(self):
			return str(self.array[1:])

	arr = np.arange(1, N+1, 1)
	np.random.shuffle(arr)
	if visualize:
		global ch1
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ch1 = ax.bar(np.arange(len(arr)), arr, 1, color='grey')
		plt.ion()
		plt.show()

	h = Heap(arr, sort=True)
	with matplotlib.rc_context(rc={'interactive': False}):
		plt.show()


if __name__ == '__main__':
	main()