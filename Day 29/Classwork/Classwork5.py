my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
print("After appending:", my_list)

my_list.insert(1, 'X')  
print("After inserting 'X' at index 1:", my_list) 

removed_element = my_list.pop() 
print("After popping last element:", my_list, "| Removed:", removed_element)  

removed_element_2 = my_list.pop(1)  

list_length = len(my_list)
print("Length of the list:", list_length)  
