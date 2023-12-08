from tqdm import tqdm
import time, os
os.chdir('c:\\Users\\user\\Desktop\\NOTES\\Level 3\\Introduction to python')
def copyfile(source, destination):
	fs = open(source, 'r')
	fd = open(destination , 'w')
	size = os.path.getsize(source)
	progess  = tqdm(range(size), f'copying {source}', unit ='8', unit_scale=True, unit_divisor=5)
	while 1:
		txt = fs.read(5)
		if txt == "":
			break
		fd.write(txt)
	fs.close()
	fd.close()
	return
if __name__ == '__main__':
	copyfile('Introduction to python', 'py3')
	
 