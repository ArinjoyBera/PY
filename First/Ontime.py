def printnum(n):
    iteration = 0
    print("The given number is n.")
    for i in range(n):
        iteration += 1
    print("The number of iterations is", iteration)

printnum(10)
printnum(20)
print("With any n the time taken and the iterations will increase.")