import sys
n= int(sys.stdin.readline())
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    s = sum(a)-a[0] 
    avg = s/a[0] 
    count = 0
    for ii in a[1:]:
        if ii > avg:
            count +=1
    b = (count/a[0])* 100
    print(f'{"%.3f" % b}%')
    

