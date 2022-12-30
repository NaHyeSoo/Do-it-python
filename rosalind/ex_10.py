fname = input("enter file: ")
#if len(fname) < 1 :
    #fname = 'clown.txt'
handle = open(fname)
di = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds :
        di[w] = di.get(w,0) + 1

x = list()
for k,v in di.items():
    c = (v,k)
    x.append(c)

x = sorted(x,reverse = True)
#print(x[:5])

for v,k in x[:5]:
    print(k,v)
