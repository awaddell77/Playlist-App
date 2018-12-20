
import os, os.path

class Playlist:
	def __init__(self):
		self._contents = []
	def __len__(self):
		return len(self._contents)
	def check_files(self):
		not_present = []
		for i in range(0, len(contents)):
			if not self._contents[i].exists:
				not_present.append(self._contents[i].path)
		if not_present:
			for i in not_present: print i+" Not found"
	def change_root(self, root):
		for item in self._contents:
			item.path = root + ":"+ os.sep + item.path

class Plist_item:
	def __init__(self, path):
		
		#self.tname = path.split(os.sep)[len(path.split(os.sep))-1] #TODO: split to stack instead\
		if os.name == 'nt': path = path.replace('/', '\\')
		self.path = path.replace('\n', '')
		self.tname = self.path.split(os.sep)[len(self.path.split(os.sep))-1]
	def stat(self):
		print(self.path)
		print(self.tname)
	def exists(self):
		return os.path.isfile(self.path)

