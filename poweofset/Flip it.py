def flipit(n1, n2):
    flips = 0
    while (n1>0) or (n2>0):
        t1 = n1&1
        t2 = n2&1
        if t1!=t2:
            flips += 1
        n1>>=1
        n2>>=1 
    return flips
Boolean = True
while Boolean:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    print("No. of flips required is", flipit(num1, num2))
    A=input("Do you want to repeat(State 'YES' or 'NO')?:")
    if A == "YES":
        Boolean=True
    else:
        Boolean=False