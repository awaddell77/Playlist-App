
import os, os.path
def reduce_path(path):
	if os.name == 'nt' and os.path.isfile(os.sep.join(path)):
		return path
	elif os.name == 'nt' and not os.path.isfile(os.sep.join(path)):
		path = path.split(os.sep)
		if len(path) < 2: return path
		root = path[0]
		path = root + os.sep + os.sep.join(path[1:])
		return reduce_path(path)
def dirs(root, files):
	dirs = []
	pass
def dirs_helper(root, p_dir, dirs):
	#if not os.path.isdir(p_dir): return
	dirs = []
	try: 
		dir_contents = os.listdir(root)
	except PermissionError as PE:
		return dirs
	print(dir_contents)

	for elem in dir_contents:
		path_tst = root + os.sep + p_dir + os.sep + elem
		print("Checking {0}".format(path_tst))
		if os.path.isdir(path_tst):
			#p_dir = root + os.sep+ p_dir + os.sep+ elem
			print("{0} is a directory".format(p_dir))
			dirs.append(path_tst)
			print("Dirs length: {0}".format(len(dirs)))
			dirs += dirs_helper(path_tst, '', dirs)
	return dirs
def search_dirs(fname, dirs, exact = True, first_match = True):
	results = ''
	for elem in dirs:
		try:
			contents = os.listdir(elem)
		except PermissionError: 
			continue
		if exact:
			print("CHECKING {0}".format(elem))
			print(contents)
			try: 
				loc = contents.index(fname)
				if first_match: return [elem + os.sep + contents[loc]]
				else: results.append(elem + os.sep + contents[loc])
			except ValueError as VE:
				continue
			
		else:

			#return
	return results

def search_dir_txt(fname, dir):

def search_f(lst,targ):
	#will be binary search eventually
	pass 
dirs = []
p_dir = 'C:\\Users\\'
s_dir = ''
dirs = dirs_helper(p_dir, s_dir, dirs)
print(len(dirs))
file_location = search_dirs('DOC#42295861.txt', dirs)
print(file_location)