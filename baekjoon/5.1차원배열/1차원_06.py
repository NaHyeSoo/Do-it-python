n = int(input())
for i in range(n):
    a = input() 
    score = 0
    sumscore = 0
    for B in a:
        if B == "O":
            score = score + 1
            sumscore = sumscore + score 
        else :
            score = 0
    print(sumscore)

# a = "roy"
# for i in a:
#     print(i)








        





