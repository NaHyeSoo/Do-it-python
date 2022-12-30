def solution(n, s):
    a = list(map(lambda x,y : y if x == True else -y, s,n))
    return sum(a)

print(solution([4,7,12],[True,False,True]))





