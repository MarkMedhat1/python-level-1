numlist = [23, 65, 19, 90]
size = len(numlist)
# size = 4
temp = numlist[1]
# temp = 65
numlist[1]=numlist[size - 1]
numlist[size - 1]=temp
print(numlist)
