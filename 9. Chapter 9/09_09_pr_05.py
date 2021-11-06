words = ['fuck', 'bad', 'aware']
with open ('sample.txt') as f:
    a = f.read()
for word in words:
    a = a.replace(word, "good")

with open ('sample.txt', "w") as f:
    f.write(a)