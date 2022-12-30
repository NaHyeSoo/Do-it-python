def abc(n):
    count = 0
    for i in range(1,n+1):
        if i < 100:
            count +=1
        else:
            # a = list(map(int.str(i)))
            # if a[0] - a[1] == a[1] - a[2] : count+=1
            if i//100 - i%100//10 == i%100//10 - i%100%10:    
                count +=1
    print(count)

print(abc(10000))


