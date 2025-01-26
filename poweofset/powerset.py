def power(set, setsize):
    powerset = (int)(2**setsize)
    outer = 0
    inner = 0
    for outer in range(0, powerset):
        for inner in range(0, setsize):
            if ((outer & (1<<inner)) > 0):
                print(set[inner])
        print("")
setsize=int(input("Enter the size of the array IMMEDIATELY ON MY COMMAND!!! :--"))
set = []
for i in range(0, setsize):
    n =int(input("Enter all the required elements R-OB-O-T PSEUDO-HUMAN-IT--Y::--_--::::"))
    set.append(n)
power(set, setsize)