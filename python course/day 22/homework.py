word="day"
word=print(word[0:1])

#2
my_list = []
for i in range(10, 21):
    my_list.append(i)

# Slicing the list with a step of 2
sliced_list = my_list[::2]

print("Original list:", my_list)
print("Sliced list with a step of 2:", sliced_list)

#3
word = input("Enter a word: ")

# Reversing the word
reversed_word = word[::-1]

print("Reversed word:", reversed_word)
    


