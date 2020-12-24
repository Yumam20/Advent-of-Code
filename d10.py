
with open('myfile.txt') as f:
    lines = [int(line.rstrip()) for line in f];

chargers = sorted(lines);
print chargers;
oneDiff = 0;
threeDiff = 1;
iterator1  = 0;
while iterator1 < len(chargers)-1:
    if chargers[iterator1 +1]-chargers[iterator1] == 1:
        oneDiff+=1;
    elif chargers[iterator1 +1] - chargers[iterator1] == 3:
        threeDiff+=1;
    iterator1+=1;
print threeDiff * oneDiff;

    