
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
print lines;