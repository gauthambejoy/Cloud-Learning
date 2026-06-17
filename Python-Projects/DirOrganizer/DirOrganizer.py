import os
import shutil
import time
import logging
logging.basicConfig(
	filename="DirOrganizer.log",
	encoding="utf-8",
	level=logging.DEBUG,
	format="%(asctime)s | %(levelname)s | %(message)s"
)
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
			print(f"{file} is moved to {ext}")
			logging.info(f"{file} is moved to {ext}")
		else:	
			os.makedirs(os.path.join(directory,ext))
			print(f"{ext} directory created")
			logging.info(f"{ext} directory created")
			shutil.move(source, destination)
			print(f"{file} is moved to {ext}")
			logging.info(f"{file} is moved to {ext}")


if __name__ == "__main__":
	directory=input("Enter the path of the directory:")
	logging.info(f"Directory path: {directory}")
	if not os.path.isdir(directory):
		print("Invalid Direcory")
		logging.error("Invalid Directory")
		exit()
	try:
		while True:
			src=os.listdir(directory)
			organize(src)
			time.sleep(5)
	except KeyboardInterrupt:
		print("Stopping the program")
		logging.info("Program Stopped")
			