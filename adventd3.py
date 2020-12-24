def countMethods(a, b):

    with open('myfile.txt') as f:
        lines = [line.rstrip() for line in f];

    c = 0;
    numTrees = 0;
    pos = 0;
    while c < len(lines):
        if c != 0:
            pos += a;
        if lines[c][pos% len(lines[c])] == '#':
            numTrees+=1;
        c+= b;
    return numTrees;


x = countMethods(1, 1);

y = countMethods(3,1);
print y;
z = countMethods(5,1);
w = countMethods(7,1);
r = countMethods(1, 2);
print(x*y*z*w*r);