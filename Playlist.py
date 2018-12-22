
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
			item_dir = item.path.split(os.sep)
			n_subs = len(item_dir)
			if n_subs <= 1: continue
			for i in range(0, n_subs):
				if os.name == 'nt':
					n_path = root + ':' + os.sep + os.sep.join(item_dir[i:n_subs])
					if os.path.isfile(n_path):
						item.path = n_path

	def _reduce_path(self, path):
		if os.name = 'nt' and os.path.isfile(os.sep.join(path)):
			return path
		elif os.name = 'nt' and not os.path.isfile(os.sep.join(path)):
			path = path.split(os.sep)
			if len(path) < 2: return path
			root = path[0]
			path = root + os.sep + os.sep.join(path[1:])
			return self._reduce_path(path)
	def _get_fext(self, fname):
		if fname not isinstance(fname, str): raise TypeError("File name must be string")
		if '.' not in fname: raise RuntimeError("No extension found in {0}".format(fname))
		return fname.split('.')[-1]
	def _get_music(self, root):
		files = []
		self._get_music_helper(files, root)
	def _get_music_helper(self, files, root):
		pass



		

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

