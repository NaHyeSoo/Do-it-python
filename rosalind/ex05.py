
x = open("rosalind_gc.txt","r")
y = x.read()
z = y.replace(">","")

dic = dict()

for i in z.split("\n"):
    if i.startswith("R"):
        a = i
        b = ""
        dic[a] = b
    else :
        # += 좌항과 우항을 더한값을 좌항에 대입
        b += i

    dic[a] = b
#print(dic)

for k,v in dic.items():
    #print(len(v))
    rate = (v.count("G") + v.count("C")) / len(v) * 100
    print(rate)
    dic[k] = rate

#print(dic)

# iterable 반복가능한 데이터 타입
# max(di,key=di.get)
# di.get = di.get(key) 해당 키에 대한 value 출력 / dic[] = dic.get()

#방법1
maxkey = max(dic,key=dic.get)
print(maxkey)

#방법2 - 이걸쓰자 !! 
for f,g in dic.items():
    if g == max((dic.values())):
        print(k)

r = max(dic.values())
print(round(r,6))
