n = input()

a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b = list(range(2,10))

## 이중리스트로 변환 후 딕셔너리 생성 
c = list()
d = list()

for i in a :
    for ii in i:
        c.append(ii)
    d.append(c)
    c = list()

di = dict(zip(b,d))

## 초 구하기 
sec = list()
for i in n:
    num = [k for k,v in di.items() if i in v]
    for i in num :
        sec.append(int(i) + 1)

print(sum(sec))
          





    