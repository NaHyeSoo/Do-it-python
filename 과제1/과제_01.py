import pandas as pd  ## pandas 모듈 불러오기 

## 파일 불러오기 / 파일을 개행문자로 줄별로 나눴음
import os

os.chdir("C:/Users/naban/Desktop/py4e/HW")

with open("example_01.txt","r") as file:
    contents = file.read().split("\n")

## 한줄씩 불러온 데이터를 tab으로 나눠 한칸씩 분리하여 리스트에 넣음  
a = list()
for i in contents : 
    a.append(i.split("\t"))

    
pd.DataFrame(a)
# for i in a:
#     print(i)






