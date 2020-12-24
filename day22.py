from collections import deque
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
print lines;
p1deck = deque();
iterator = 1;
winnerVal = 0;
while iterator < len(lines):
    if lines[iterator] == '':
        break;
    else:
        p1deck.append(int(lines[iterator]));
    iterator += 1;
iterator += 2;
p2deck = deque();
while iterator < len(lines):
    if lines[iterator] == '':
        break;
    else:
        p2deck.append(int(lines[iterator]));
    iterator += 1;
print p1deck;
while p1deck and p2deck :
    val1 = p1deck.popleft();
    val2 = p2deck.popleft();
    if val1 > val2:
        p1deck.append(val1)
        p1deck.append(val2);
    else:
        p2deck.append(val2)
        p2deck.append(val1);
if not p1deck :
    i = 1;
    while p2deck :
        winnerVal += i*p2deck.pop();
        i+= 1;
elif not p2deck :
    i = 1;
    while p1deck :
        winnerVal += i*p1deck.pop();
        i += 1;
print winnerVal;

