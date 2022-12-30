n = int(input())
c = 1
for i in range(n) : 
    a,b = map(int,input().split())
    print(f'Case #{c}: {a+b}')
    c = c+1