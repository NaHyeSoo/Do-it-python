file = open("rosalind_revc.txt","r")
a = file.read()
b = a.rstrip()
c = b[::-1]
#c는 역서열!!!
#print(c)

newseq = ""
dna = {"A":"T","T":"A","G":"C","C":"G"}
for base in c:
    if base in dna:
        newseq = newseq + dna[base]
print(newseq)
















#리스트 - reverse랑 replace이용?
