def solution(nums:list):
    answer = sorted(set([a+b for a in nums for b in nums[nums.index(a)+1:]])) 
    return answer

print(solution([2,1,3,4,1]))    