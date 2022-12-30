'''

import pandas as pd
import os

os.chdir("C:/Users/naban/Desktop/py4e/HW")

with open("example_01.txt", "r") as file:
    contents = file.read().split("\n")

a = list()
for i in contents:
   a.append(i.split("\t"))


for i in range(len(a)):
    del a[i][0]

# print(a)
print(pd.DataFrame(a))
# for i in a:
#     print(i)

'''


print("hello")