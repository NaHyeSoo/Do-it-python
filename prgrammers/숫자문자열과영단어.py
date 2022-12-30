def solution(s:str):
    di = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}  

    for i in di.keys() :
        if i in s :
            s = s.replace(i,di.get(i))
    return int(s)        
   
print(solution("one4seven"))    

