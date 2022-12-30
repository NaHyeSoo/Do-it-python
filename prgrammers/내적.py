def solution(a:list, b:list):
    c = [x*y for x,y in zip(a,b)]  
    answer = sum(c)
    return answer

'''
 c = dict(zip(a,b))
 d = [k*v for k,v in c.items()]
answer = sum(d)

dict 이용하면 키가 겹칠 수 있어서 결과 오류 

'''



print(solution([1,2,3,4],[-3,-1,0,2]))

print(solution([-1,0,1],[1,0,-1]))