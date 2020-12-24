
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
#print lines;
acc =0 ;
lineN = 0;
visited = [];
lookupdict = {"acc": 1, "jmp" : 2, "nop":3}
while lineN < len(lines):
    
    visited.append(lineN);
    k = lookupdict[lines[lineN][0:3]];
    if k == 1:
        acc += int(lines[lineN][4:])
        lineN += 1;
            
    if k == 2:
        
        x =int(lines[lineN][4: ])
        if lineN+x in visited:
            lineN += 1;
        else:
            lineN += x;

    if k == 3:
        if lineN+1 in visited:
            lineN += int(lines[lineN][4:]);
        else:
            lineN += 1;
print acc;
        