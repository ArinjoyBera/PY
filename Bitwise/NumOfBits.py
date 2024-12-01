def NumberofBits(a):
    count = 0
    while (a):
        count+=1
        a>>=1
    return count
num = int(input("Enter a number:"))
print("The number of bits are", NumberofBits(num))