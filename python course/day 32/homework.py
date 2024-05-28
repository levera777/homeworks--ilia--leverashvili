#1
def manual_index(numbers_list, search_value):
    for index, value in enumerate(numbers_list):
        if value == search_value:
            return index
    return -1

# Example usage:
numbers_list = [10, 20, 30, 40, 50]
search_value = 30

print(manual_index(numbers_list, search_value))  # Output: 2

#2
def manual_max(numbers_list):
    if not numbers_list:
        raise ValueError("The list is empty.")
    
    max_value = numbers_list[0]
    for number in numbers_list:
        if number > max_value:
            max_value = number
    return max_value

# Example usage:
numbers = [10, 20, 30, 40, 50]
print(manual_max(numbers))  # Output: 50

#3
def manual_pop(numbers_list, index):
    if index < 0 or index >= len(numbers_list):
        raise IndexError("Index out of range.")
    
    new_list = []
    for i in range(len(numbers_list)):
        if i != index:
            new_list.append(numbers_list[i])
    
    return new_list

# Example usage:
numbers = [10, 20, 30, 40, 50]
index_to_remove = 2

print(manual_pop(numbers, index_to_remove))  # Output: [10, 20, 40, 50]