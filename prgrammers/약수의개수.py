def solution(left, right):
    a = list(range(left,right+1))
    lst = list()
    for i in a :  
        cnt = 0
        for m in range(1,i):
            if i % m == 0 :
                cnt += 1
        lst.append(cnt)
            
    return lst


print(solution(13,17))    


  