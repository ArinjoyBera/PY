a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
anb=a&b
boc=b|c
bnc=b&c
bocnbnc=boc&bnc
q=anb|bocnbnc
print(q, "is the last output.")