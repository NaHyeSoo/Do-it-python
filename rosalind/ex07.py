file = open("rosalind_iprb.txt","r")
x = file.read()
x = x.rstrip()
a = x.split()
#print(a)
k = int(a[0])
m = int(a[1])
n = int(a[2])

s = k + m + n
#print(s)

#nn
p1 = n / s * (n-1) / (s-1)
#mn
p2 = m / s * n / (s-1)
#mm
p3 = m / s * (m -1) / (s-1) * 1 / 4

tp = 1 - (p1 + p2 + p3)
print(round(tp,5))
