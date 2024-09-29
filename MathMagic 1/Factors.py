def factor(num):
    numb = 0
    for i in range (1, num+1):
        if num%i == 0:
            print(i)
            numb += 1
    print("The total number of factors are", numb)
num = int(input("Enter the number:"))
factor(num)