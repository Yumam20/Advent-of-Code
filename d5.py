
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
print lines;
stack = [];
for i in lines:
    i = i.replace('B', '1').replace('F', '0').replace("R", "1").replace("L", "0")
    x = int(i[0:7], 2);

    y = int(i[7:10], 2);
    
    stack.append(x*8 + y);
print max(stack);

for i in range(0,8*127 + 9):
    if i not in stack and i+1 in stack and i-1 in stack:
        print i;


