fname = input("enter file: ")

handle = open(fname)
di = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds :
        di[w] = di.get(w,0) + 1
        #oldcount = di.get(w,0)
        #newcount = oldcount + 1
        #di[w] =  newcount
        # 위  세 줄 통합하여...
#print(di)


maxcount = None
maxkey = None
for key,count in di.items():
    if maxcount is None :
        maxcount = count
        maxkey = key
    if count > maxcount :
        maxcount = count
        maxkey = key
print(maxkey,maxcount)
