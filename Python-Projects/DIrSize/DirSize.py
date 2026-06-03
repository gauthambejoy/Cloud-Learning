import os

path=input("Enter the Directory path:")

total = 0

for file in os.scandir(path):
    if file.is_file():
        size=os.path.getsize(file.path)
        print(f"{file.name} -> {size} bytes")
        total+=size


print(f"Size of Directory is: {total}")
