import os

os.chdir("C:/Users/naban/Desktop/py4e/HW")

with open("example_01.txt","r") as file:
    contents = file.read().split("\n")

## 한줄씩 불러온 데이터를 tab으로 나눠 한칸씩 분리하여 리스트에 넣음 (이중리스트)
originaldata = list()
for i in contents : 
    originaldata.append(i.split("\t"))

realdata = list()
for i in contents : 
    realdata.append(i.split("\t"))

## head 없애주기 
originaldata = originaldata[1:][:]

trait_1 = []
trait_2 = []
trait_3 = []
trait_4 = []
trait_5 = []


for i in range(len(originaldata)):
    if originaldata[i][0] == '1':
        trait_1.append(originaldata[i][:])

        

for i in range(len(originaldata)):
    if originaldata[i][0] == '2':
        trait_2.append(originaldata[i][:])

for i in range(len(originaldata)):
    if originaldata[i][0] == '3':
        trait_3.append(originaldata[i][:])

for i in range(len(originaldata)):
    if originaldata[i][0] == '4':
        trait_4.append(originaldata[i][:])

for i in range(len(originaldata)):
    if originaldata[i][0] == '5':
        trait_5.append(originaldata[i][:])



            