n = int(input())
group = n

for i in range(n):
    word = input()  
    for index in range(len(word)):
        try :
            if word[index] == word[index+1]:
                pass
            elif word[index] in word[index+1:]:
                group -= 1
                break
        except : pass    


print(group)

