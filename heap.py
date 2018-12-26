class Heap:
	def __init__(self, l=[], compare_=lambda x, y : x<y):
		self.array = [0]
		self.length = 0
		self.compare = compare_
		for e in l:
			self.enque(e)

	def enque(self, a):
		self.array.append(a)
		self.length += 1
		self.__upcheck(self.length)

	def deque(self):
		self.__swap(1, 0) #first and last
		ret = self.array.pop()
		self.length -= 1
		self.__downcheck(1)
		return ret

	def __swap(self, a,b):
		if a == b:
			return
		self.array[b], self.array[a] = self.array[a], self.array[b]

	def __upcheck(self, index):
		parent = index//2
		if self.compare(self.array[parent], self.array[index]) and index >= 1:
			self.__swap(index, parent)
			self.__upcheck(parent)

	def __downcheck(self, index):
		left = 2*index
		right = 2*index+1
		largest = index
		if left < self.length and self.compare(self.array[index], self.array[left]):
			largest = left
		if right < self.length and self.compare(self.array[index], self.array[right]):
			largest = right
		self.__swap(largest, i)
		self.__downcheck(largest)

if __name__ == '__main__':
	h = Heap()
	h.enque(1)
	print(h)
