fname = input("enter file: ")
if len(fname) < 1 :
    fname = 'clown.txt'
handle = open(fname)
for line in handle:
    line = line.rstrip()
    print(line)
