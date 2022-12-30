file = open("rosalind_hamm.txt","r")
x = file.read()
y = x.rstrip()
y = y.split("\n")
a = y[0]
b = y[1]
a = list(a)
b = list(b)

num = 0
roy = list(range(0,len(a)))

for n in roy:
    if a[n] != b[n]:
        num = num + 1

print(num)
