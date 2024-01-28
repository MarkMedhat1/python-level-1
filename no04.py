lst =[1,6,3,6,3,6]
num = int(input("enter the num : "))
count_num = 0
for element in lst :
    if element == num :
      count_num += 1
print("number appear in the list time: "+ str(count_num))