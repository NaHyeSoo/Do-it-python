# ## 문자열 6번 문제
# s = input().split()
# print(len(s))

## 문자열 7번 문제 
a,b = input().split()

a = a[::-1]     
b = b[::-1]     

# a = ''.join(reversed(a))
# b = ''.join(reversed(b))

if int(a) > int(b):
    print(int(a))
else:
    print(int(b))    