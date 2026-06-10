import os
import shutil
import time

def organize(src):
	for file in src:
		if os.path.isdir(os.path.join(directory,file)):
			continue
		name, ext=os.path.splitext(file)
		ext=ext[1:]
		source=os.path.join(directory,file)
		destination=os.path.join(directory,ext,file)
		
		if ext=='':
			continue
		if os.path.exists(os.path.join(directory,ext)):
			shutil.move(source, destination)
		else:	
			os.makedirs(os.path.join(directory,ext))
			shutil.move(source, destination)


if __name__ == "__main__":
	directory=input("Enter the path of the directory:")
	while True:
		src=os.listdir(directory)
		organize(src)
		time.sleep(5)