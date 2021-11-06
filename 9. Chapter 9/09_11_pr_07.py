a = True
v = 1
with open("log.txt") as f:
    while a:
        a = f.readline()
        if 'python' in a.lower():
            print(a)
            print(f"Yes python is present on line number {v}") 
        v+=1