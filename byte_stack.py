class Byte_queue:
	def __init__(self):
		self.__length = 0
		self._contents = bytes()
	def offer(self, x):
		self._contents += x
		self.__length += 1
	def remove(self):
		if self.__length == 0: return
		item = self.contents[0]
		self.__length -= 1
		return item