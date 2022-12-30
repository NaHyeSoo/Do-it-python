file = open("rosalind_fib.txt","r")
a = file.read()
b = a.split()
#b는 리스트/ 위치값 이용해서 값 할당

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo(n-1) + fibo(n-2) * int(b[1])

x = fibo(int(b[0]))
print(x)
