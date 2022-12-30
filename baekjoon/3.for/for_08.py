n = int(input())
num = 1
for i in range(n) : 
    a,b = map(int,input().split())
    print(f'Case #{num}: {a} + {b} = {a+b}')
    num = num+1