file = open("rosalind_rna.txt","r")
a = file.read()

y = a.replace("T","U")
print(y)
