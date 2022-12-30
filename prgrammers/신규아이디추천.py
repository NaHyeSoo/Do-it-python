def solution(new_id:str):
    # 1,2단계
    a = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']   
    b = list(new_id.lower())
    # c = [ i for i in b if i not in a]
    c = list(filter(lambda x : x not in a, b))

    ## 3단계 '.반복 지우기 
    d = list()
    for i in range(len(c)):
        try:
            if c[i] == "." and c[i] == c[i+1]:
                pass
            else :
                d.append(c[i])
        except :
            d.append(c[i])
             

    # 4단계 / 5단계
    try:    
        if d[0] == "." :
            del d[0]
        if d[-1] == ".":
            del d[-1]
    except:
        pass        

    if not d :
        d = list("a")    

    # 6단계
    if len(d) >= 16 :
        del d[15:]
        if d[14] == ".":
            del d[14]

    # 7단계
    if len(d) < 3 :
        d.append(d[-1] * (3-len(d)))
    answer = ''.join(d)   

    return answer




print(solution("...!@BaT#*..y.abcdefghijklm"))