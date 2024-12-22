def getridofxor(arr):
    res = 0
    for element in arr:
        res = res^element
    return res
arr = []
n = int(input("Enter the array size of your free random choice:"))
while n:
    num = int(input("Enter any random number<<<NO PERSUASION>>>:"))
    arr.append(num)
    n -= 1
print("The one odd occuring number is", getridofxor(arr))