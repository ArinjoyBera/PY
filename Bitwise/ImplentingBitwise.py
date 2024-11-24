def fun(a, b):
    print(a, "and", b, "is", a&b)
    print(a, "or", b, "is", a|b)
    print(a, "xor", b, "is", a^b)
    print(a, "not is", ~a)
    print(b, "leftshift 5 is", b<<5)
    print(a, "rightshift 5 is", a>>5)

a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
fun(a, b)