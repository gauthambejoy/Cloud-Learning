import os

dir=input("Enter the directory path:")

for count,filename in enumerate(os.listdir(dir)):
    rnm=f"File.{count}.txt"

    src=f"{dir}/{filename}"
    dst=f"{dir}/{rnm}"

    os.rename(src,dst)                                                                  