def leftRotate(arr, d, n): 
    for i in range(gcd(d,n)): 
          
        # move i-th values of blocks  
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 
def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a%b) 
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
dirDict = [0,0,0,0]; 
# N = 0, E = 1, S = 2, W = 3
pos = 0;
waypoint = [1,10,0,0];
curdir = 1;
while pos < len(lines):
    k = lines[pos][0];
    if k == 'F':
        x = int(lines[pos][1:]);
        iterator = 0;
        while iterator < 4:
            dirDict[iterator] = dirDict[iterator] + waypoint[iterator]*x;
            iterator+=1;
    if k == 'N':
        waypoint[0] += int(lines[pos][1:]);
    if k == 'S':
        waypoint[2] += int(lines[pos][1:]);
    if k == 'E':
        waypoint[1] += int(lines[pos][1:]);
    if k == 'W':
        waypoint[3] += int(lines[pos][1:]);
    if k == 'R':
        s = int(lines[pos][1:])/90;
        leftRotate(waypoint, 4-s, 4);
    if k == 'L':
        s = int(lines[pos][1:])/90;
        leftRotate(waypoint, s, 4);
    pos+= 1;
    print dirDict;
print abs(dirDict[0]-dirDict[2]) + abs( dirDict[1]  -dirDict[3]);
        
