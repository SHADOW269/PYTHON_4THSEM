def find_elements(list1):
    unique_list = []
    for element in list1:
        if list1.count(element) == 1:
            unique_list.append(element)
    return unique_list
N = int (input("Enter the number of elements in the list: "))
My_list = []
for i in range(N):
    element = int (input(f"Enter element {i + 1}:"))
    My_list.append(element)
print(f"The element in the list are : {My_list}")
unique_element = find_elements (My_list)
print(f"Unique element in the list: {unique_element}")