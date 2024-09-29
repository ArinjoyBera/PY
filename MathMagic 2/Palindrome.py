def palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        rem = temp%10
        reverse = reverse*10 + rem
        temp//=10
    if reverse == num:
        print(num, "is a palindrome number. CONGRATS!!!CONGRATS!!!CONGRATS!!!")
    else:
        print("Why you!!!")
num = int(input("Enter a Palindrome number THIS INSTANT!!!"))
palindrome(num)