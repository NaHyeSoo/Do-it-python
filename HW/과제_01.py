import pandas as pd  ## pandas 모듈 불러오기 

## 파일 불러오기 / 파일을 개행문자로 줄별로 나눴음
import os

os.chdir("C:/Users/naban/Desktop/py4e/HW")

with open("example_01.txt","r") as file:
    contents = file.read().split("\n")

## 한줄씩 불러온 데이터를 tab으로 나눠 한칸씩 분리하여 리스트에 넣음 (이중리스트)
originaldata = list()
for i in contents : 
    originaldata.append(i.split("\t"))

#print(originaldata)    
    
# print(pd.DataFrame(originaldata))

# for i in originaldata:
#  print(i)

### 데이터를 trait별로 구분하기
trait_1 = []

# for i in range(1,len(originaldata)-1):
#     if originaldata[i][0] == '1':
#         trait_1.append(originaldata[i][:])
       


    








