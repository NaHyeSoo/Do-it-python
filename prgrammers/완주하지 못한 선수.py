"""
def solution(participant, completion):
    for i in completion:
        if i in participant :
            participant.remove(i)
        return participant[0]
 
lst = ["a","a","b"]
lst.remove("a")
print(lst) # [a,b]

### 시간초과 

"""

'''
def solution(p, c):
    a = set(p)
    b = set(c)
    if a != b:                                     ## 동명이인이 answer가 아닐때
        answer = list(a - b)
    else :                                                   ## 동명이인이 ANSWER일때
        a = list(set([i for i in p if p.count(i)>1]))       
        answer = [i for i in a if c.count(i) == 1 ]
    return answer[0]

'''

#print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
#print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

a = ["leo", "kiki", "eden","leo"]
# b = dict()
# for i in a :
#     if i in b :
#         b[i] = b[i] + 1
#     else:
#         b[i] = 1    

# print(b)    

# b = {k:a.count(k) for k in a}    
# print(b)

'''
def solution(p, c):
    if set(p) != set(c):                  ## 동명이인이 answer가 아닐때
        answer = list(set(p) - set(c))
    else :              
        p_dict = {k:p.count(k) for k in p}  
        c_dict = {k:c.count(k) for k in c}
        answer = [k for k,v in p_dict.items() for a,b in c_dict.items() if v != b ]
    return answer[0]    

'''

#print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))



# def solution(p, c):
#     p = sorted(p)
#     print(p)
#     c = sorted(c)
#     print(c)
#     for i in range(len(c)):
#         try :
#             if p[i] != c[i]:
#                 answer = [p[i]]
#         except :
#             answer = [p[len(p)-1]]
    
#     return answer[0]        



def solution(p, c):
    p = sorted(p)
    c = sorted(c)
    for i in range(len(c)):
        if p[i] != c[i]:
            answer = [p[i]]
            break
    else:
        print("p:", p)
        return p[-1]

    return answer[0]  


print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
