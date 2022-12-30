def solution(array, commands):
    answer = list()
    for a,b,c, in commands :
        a = a-1
        c = c-1  
        ans = sorted(array[a:b])[c]
        answer.append(ans)
    return answer

def solution2(array, commands):
    answer = [sorted(array[a-1:b])[c-1] for a,b,c, in commands]
    return answer   

def solution3(array, commands):
    answer = list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1] , commands))
    return answer   

'''
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
for a,b,c in com:
    print(a,b,c)

반복변수 3개도 가능하네!!    

'''

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
print(solution2([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
print(solution3([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))