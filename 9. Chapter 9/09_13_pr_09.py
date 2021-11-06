File1 = "copy.txt"
File2 = "this.txt"

with open("copy.txt") as f:
    F1 = f.read()

with open("this.txt") as f:
    F2 = f.read()

if F1==F2:
        print("Files are identical")
else:
        print("Files are not identical")