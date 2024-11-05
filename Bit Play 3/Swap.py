def swap(a, b):
    a = a^b
    print(a)
    b = b^a
    print(b)
    a = a^b
    print("After swapping a", a)
    print("After swapping b", b)
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
swap(a, b)