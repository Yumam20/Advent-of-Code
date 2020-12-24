from collections import deque


def method():
    with open('myfile.txt') as f:
        lines = [line.rstrip() for line in f];
    print lines;
    earliestTime = int(lines[0]);
    earliestTimeITR = earliestTime;
    itr = 1;
    busvals = [];
    offset = [];
    while itr < len(lines):
        parsed = lines[itr].rsplit(",");
        i = 0;
        while i < len(parsed):
            if parsed[i].isdigit():
                busvals.append(int(parsed[i]));
                offset.append(i);
            i += 1;
        itr += 1;
    print busvals;
    print offset;
    
    while earliestTimeITR > 0:
        returnMe = True;
        itr1 = 0;
        print earliestTimeITR;
        while itr1 < len(busvals):
            returnMe = returnMe and ((earliestTimeITR + offset[itr1]) % busvals[itr1] == 0)
            itr1 += 1;
        if returnMe: 
            print "end";
            return;
        earliestTimeITR += 1;
method();



    