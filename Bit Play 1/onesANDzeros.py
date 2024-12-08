def numofbits(n):
    ones = 0
    zeros = 0
    while n:
        if ((n&1)==1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print("The number of ones is ", ones)    
    print("The number of zeros is ", zeros)
a = int(input("Enter any random number that comes to your mind : "))
numofbits(a)