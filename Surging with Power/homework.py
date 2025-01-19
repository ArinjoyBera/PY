def nnrjr(number):
    count = 0
    if ((number & (~(number-1))) == number):
        while (number > 1):
            number>>=1
            count += 1
        if count%3 == 0:
            return True
        else:
            return False
NNRJR = int(input("Enter a nnrjr number:"))
if nnrjr(NNRJR)==True:
    print(NNRJR, "is a power of 8.")
elif nnrjr(NNRJR)==False:
    print(NNRJR, "is not a power of 8.")