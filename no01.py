numbers_list = [15,16,20,3,9,20]
count_Even =0
count_odd =0
sum_Even = 0
sum_odd = 0
for item in  numbers_list:
    if item %2 == 0 :
     sum_Even = sum_Even+ item
     count_Even = count_Even +1
    else :
     sum_odd = sum_odd + item
     count_odd = count_odd +1
print("Sum even = " + str(sum_Even))
print("count even = "+str(count_Even))
print("sum odd = "+str(sum_odd))
print("count odd ="+str(count_odd))
