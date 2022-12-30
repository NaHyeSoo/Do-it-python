def selfnum() :
    a = set(range(1,10001))
    b = set()

    for i in range(1,10001):
        for ii in str(i): 
            i += int(ii)
        b.add(i) # 이 구문이 위의 for문에 결합되면 안됨     
# 저게 for ii 안에 있으면 예를 들어 85 85+8값도 들어가고  85+8+5값도 b에 들어가게됨!!

    c = a - b
    self = sorted(c)
    for i in self:
        print(i)

selfnum()

# a = set(range(1,11))
# b = set()
# for i in range(1,11):
#     for ii in str(i): 
#         i += int(ii)
#         b.add(i)  # 이 구문이 위의 for문에 결합되면 안됨
        
# print(b)



        
   




