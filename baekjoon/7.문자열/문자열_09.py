s = input()
croa = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in croa :
    if i in s:
        s = s.replace(f'{i}',"1")

print(len(s))


# a = "abc"
# if "ab" in a :
#     a = a.replace("ab","ar")