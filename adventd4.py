def byrvalid(str):
    x = str.find("byr:")
    if (x == -1): 
        return False;
    yr = int(str[x+4:x+8]);
    if yr < 1920 or yr > 2002:
        return False;
    return True;

def iyrvalid(str):
    x= str.find("iyr:") 
    if x == -1: 
        return False;
    yr = int(str[x+4:x+8]);
    if yr < 2010 or yr > 2020:
        return False;
    return True;
def eyrvalid(str):
    x= str.find("eyr:") 
    if x == -1: 
        return False;
    yr = int(str[x+4:x+8]);
    if yr < 2020 or yr > 2030:
        return False;
    return True;
def hgtvalid(str):
    x= str.find("hgt:") 
    if x == -1: 
        return False;
    y = str.find(" ", x);
    if str[y-2:y] == "cm":
        height = int(str[x+4:y-2]);
        if height < 150 or height > 193:
            return True;
    if str[y-2:y] == "in":
        height = int(str[x+4:y-2]);
        if height < 59 or height > 76:
            return True;
    return False;

def hclvalid(str):
    x= str.find("hcl:") 
    if x == -1: 
        return False;
    if str[x+4] != '#':
        return False;
    return str[x+5:x+11].isalnum();

def eclvalid(str):
    x= str.find("ecl:") 
    if x == -1: 
        return False;
    valids = "amb blu brn gry grn hzl oth".rsplit(" ");
    value = str[x+4:x+7];
    if value not in valids:
        return False;
    return True;
def pidvalid(str):
    x= str.find("pid:") 
    if x == -1: 
        return False;
    return str[x+4:x+13].isdigit();

with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
print lines;
iterator = 0;
numPassports = 0;
byr = False; iyr = False; eyr = False; hgt = False; hcl = False; ecl = False; pid = False; 
while iterator < len(lines):
    if(lines[iterator] == ''):
        byr = False; iyr = False; eyr = False; hgt = False; hcl = False; ecl = False; pid = False;
    byr = byr or byrvalid(lines[iterator]);
    iyr = iyr or iyrvalid(lines[iterator]);
    eyr = eyr or eyrvalid(lines[iterator]);
    hgt = hgt or hgtvalid(lines[iterator]);
    hcl = hcl or hclvalid(lines[iterator]);
    ecl = ecl or eclvalid(lines[iterator]);
    pid = pid or pidvalid(lines[iterator]);
    if(byr and iyr and eyr and hgt and hcl and ecl and pid):
        numPassports += 1;
        byr = False; iyr = False; eyr = False; hgt = False; hcl = False; ecl = False; pid = False;
        iterator += 1;
    
    iterator += 1;

print numPassports;
