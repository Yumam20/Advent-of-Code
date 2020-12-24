
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f];
print lines;
goodPasswords = 0 ;
for x in lines:
    x = x.replace(": ", " ").replace("-", " ")    # Converts gaps between data to spaces
    x = x.split(" ")  # Splits string into a list of the data in string form
    min_times = int(x[0]) -1
    max_times = int(x[1]) -1
    target_char = x[2]
    password = x[3]
    x = (password[min_times] == target_char);
    y = (password[max_times] == target_char);

    if x ^ y:
        goodPasswords += 1
print goodPasswords;

