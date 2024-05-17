def categorize_strings(strings):
    odd = []
    even = []
    
    for string in strings:
        if len(string) % 2 == 0:
            even.append(string.upper())
        else:
            odd.append(string.upper())
    
    return odd, even

# Example usage:
strings = ["ilia", "nika", "beno", "dachi", "python", "hello"]
odd, even = categorize_strings(strings)

print("Strings with odd number of letters:", odd)
print("Strings with even number of letters:", even)

#2



def process_strings(strings):
    new_list = []

    for string in strings:
        if len(string) % 2 == 0:
            new_list.append(string.upper())
        else:
            new_list.append(string[0].upper() + string[1:].lower())

    return new_list

# Example usage:
strings = ["vano", "nika", "bubazi", "zauri", "python", "code"]
result = process_strings(strings)

print("Processed list of strings:", result)


#3


def convert_case(strings):
    converted_list = []

    for string in strings:
        if string.isupper():
            converted_list.append(string.lower())
        elif string.islower():
            converted_list.append(string.upper())

    return converted_list

# Example usage:
strings = ["saba", "LUKA", "LEVER", "gio"]
result = convert_case(strings)

print("Converted list of strings:", result)


#4


def process_string(input_string):
    index = input_string.find(' ')
    if index % 2 == 0:
        return input_string.upper()
    else:
        return input_string.capitalize()

# Example usage:
input_str = "this is a test string"
result = process_string(input_str)
print("Processed string:", result)

#end


