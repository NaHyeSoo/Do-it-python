import os

os.chdir("C:/Users/naban/Desktop/py4e/rosalind")

with open("rosalind_dna.txt") as f:
    a = f.read()

print(a.count("A"), a.count("C"), a.count("G"), a.count("T"))
