a = int(input("You!! Enter the one and only number:"))
b = int(input("You!! Enter the last but not the least number:"))
gcd = 1
for i in range(1, min(a, b)+1):
    if a%i==0 and b%i==0:
        gcd = i
print("gcd of", a, "and", b, "is", gcd)