while True:
    num = int(input("Enter the number:"))
    temp = num
    result = 0
    while temp > 0:
        rem = temp%10
        result = result + rem**3
        temp = temp//10
    if num == result:
        print(num, "is an armstrong number.")
    else:
       print(num, "is not an armstrong number.")