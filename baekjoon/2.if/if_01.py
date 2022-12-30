## a,b = int(input().split()) 이거 안됨
## int는 리스트를 정수형으로 바꿔줄 수 없음
## map(적용할 함수, 반복가능한 자료형)
a,b = map(int,input().split())

#print(a)
#print(b)

if a > b :
    print(">")
elif a < b :
    print("<")
else :
    print("==") 
