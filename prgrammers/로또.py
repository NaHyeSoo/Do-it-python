def solution(lottos, win_nums):
    a = lottos.count(0)
    b = 0
    for i in lottos :
        if i in win_nums:
            b += 1   
    # b = len(set(lottos)&set(win_nums) 
       
    best = 7 - (a+b) if a+b != 0 else 6
    worst = 7 - b if b != 0 else 6

    answer = [best,worst]
    return answer



print(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19])) 
print(solution(	[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))   