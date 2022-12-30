n = int(input())
a = list(map(int,input().split()))
#print(a)

m = max(a)
for ii in range(n):
    a[ii]=  a[ii]/m*100
#print(a)
print(sum(a)/len(a))

