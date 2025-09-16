my_list = [5,2,3,1,4]
my_list2 = ["a","b","c"]


greatest = max(my_list)
smallest = min (my_list)

print (f" the greatest number in the list{greatest}" )
print(f"the smallest number in the list{smallest}" )

list_sum = sum (my_list)
print (f"The sum of all numbers in the list {list_sum}" )


my_list_lenght = len (my_list)
print(f"The lenght of my list is {my_list_lenght}" )

in_order = sorted(my_list) 
print(f" My sorted list {in_order}")
def filter_prize (prize):
if (prize > 400 ):
 return True 
else:
    return False 

    item_price = [230,400,450,350,370]
filtered_prize = filter (filter_prize,item_prize)
print( filtered_prize)