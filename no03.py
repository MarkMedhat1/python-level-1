list = [1,6,3,5,3,4]
num = int(input("enter num : ") )
if num in list :
 #index = list.index(num)
 print(str(num) +' is found on index ' , str(list.index(num)))
else:
 print('number is not found')