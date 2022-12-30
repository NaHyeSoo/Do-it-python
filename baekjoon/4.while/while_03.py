a = b = int(input())
count = 0
while True:
    ten = a//10
    one = a%10
    sum = ten + one 
    count = count + 1
    a = int(str(one)+str(sum%10))
    if a == b:
        print(count)
        break






  


  
