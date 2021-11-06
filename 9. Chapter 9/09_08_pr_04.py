with open ('sample.txt') as f:
    a = f.read()

a = a.replace("bad", "good")

with open ('sample.txt', "w") as f:
    f.write(a)