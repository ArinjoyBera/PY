def nnrjr(number):
    if number == 0:
        return 0
    elif ((number & (~(number-1))) == number):
        return 1
    return 0
NNRJR = int(input("Enter a nnrjr number:"))
if nnrjr(NNRJR)==True:
    print(NNRJR, "is a power of 2.")
elif nnrjr(NNRJR)==False:
    print(NNRJR, "is not a power of 2.")