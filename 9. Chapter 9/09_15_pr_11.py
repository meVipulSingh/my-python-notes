import os
oldname = 'sample2.txt'
newname = 'renamed_by_python.txt'
with open(oldname) as f:
    a = f.read()

with open(newname, 'w') as f:
    f.write(a)

os.remove(oldname)