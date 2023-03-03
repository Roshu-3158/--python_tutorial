# when we use with block there is no need to close the file it automatically closed
with open("33_file.txt") as f:
    a = f.read()
    print(a)
