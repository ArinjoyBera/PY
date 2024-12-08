def setOrnot(number, nbit):
    if number & (1 << (nbit-1)):
        return "SET"
    else:
        return "NOT SET"
number = int(input("Enter a number:"))
nbit = int(input("Enter the bit number:"))
print("The bit is", setOrnot(number, nbit))