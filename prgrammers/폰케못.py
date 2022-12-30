def solution(nums):
    n = int(len(nums) / 2)
    s = len(set(nums))
    if s < n :
        return s
    else :
        return n    
    

print(solution([3,1,2,3])) 
print(solution([3,3,3,2,2,4]))      
print(solution([3,3,3,2,2,2]))    