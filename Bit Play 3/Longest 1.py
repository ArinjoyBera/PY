def num(num):
    count = 0
    while num != 0:
        num = num & (num << 1 )
        count += 1
    return count
num11 = int(input("Enter a number whatsoever:"))
print("Longest consecutive 1's length", num(num11))