def printnum(n):
    iteration = 0
    print("The given number is n.")
    for i in range(n):
        for j in range(i):
            iteration += 1
    print("The number of iterations is", iteration)

printnum(10)
printnum(20)
print("For every n the time taken equals n^2.")