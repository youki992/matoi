with open("data.txt", 'r') as f:
    len1 = len(f.readlines())
with open("num.txt", 'r') as f:
    len2 = f.read()
with open("num.txt", 'w') as f:
    f.write(str(len1+int(len2)-1))