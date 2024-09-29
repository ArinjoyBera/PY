def sieveoferosthenes(u, l):
    prime = [True for i in range(l, u)]
    p = l
    print(p)
    while (p*p <= u):
        if prime[p] == True:
            for i in range(p*p, u, p):
                print(i)
                prime[i] = False
        p += 1
    for p in range(2, u):
        if prime[p]:
            print(p)
upper = int(input("Enter the upper limit:"))
lower = int(input("Enter the lower limit:"))
sieveoferosthenes(upper, lower)