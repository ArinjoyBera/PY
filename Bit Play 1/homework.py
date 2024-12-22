def bitsandnum(n):
    count = 1
    while n:
        if ((n&1)==1):
             return count 
        n>>=1
        count+=1
    return count
n = int(input("Enter a number:"))
print("The set bit is", bitsandnum(n))
