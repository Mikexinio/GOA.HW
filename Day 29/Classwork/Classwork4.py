list1 = [10, 20, 30, 40, 50]
list2 = ['a', 'b', 'c', 'd', 'e']

removed_from_list1_1 = list1.pop()  
removed_from_list1_2 = list1.pop(2) 

removed_from_list2_1 = list2.pop()  
removed_from_list2_2 = list2.pop(1)  

print("Updated List 1:", list1)
print("Removed from List 1:", removed_from_list1_1, "and", removed_from_list1_2)

print("Updated List 2:", list2)
print("Removed from List 2:", removed_from_list2_1, "and", removed_from_list2_2)
