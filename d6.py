from collections import deque
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
print lines;
counter = 0;
tempQ = deque();
for x in lines:
    if x == '':
        counter += len(tempQ);
        tempQ.clear();
    else: 
        for charInsert in x:
            if charInsert not in tempQ:
                tempQ.append(charInsert);
print counter;