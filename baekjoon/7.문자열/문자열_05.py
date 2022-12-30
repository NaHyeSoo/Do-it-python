s = input().upper()
lst = list()
a = set()


### 중복제거한 문자열 set 
for i in s:
    a.add(i) 

### 원래 문자열 개수 구하기 
for i in sorted(a):
    lst.append(s.count(f'{i}'))

### 문자와 문자별 개수 딕셔너리 생성 
b = set(lst)

c = dict(zip(sorted(a),lst))
d = [k for k,v in c.items() if v == max(b)]

### 최댓값이 2개 이상이면 ? 출력 
if len(d) > 1 :
    print("?")
else :
    print(d[0])    
    
     
        

 