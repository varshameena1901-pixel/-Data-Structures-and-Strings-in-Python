# Demonstrate list slicing

#Create a list of number from 1 to 10

numbers = list(range(1,11))
print("Original list:", numbers)

#extract the first five elements

first_five = numbers[:5]
print("Extracted first five elements:", first_five)

#reverse the extracted list

reversed_list = first_five [::-1]
print("Reversed extracted elements:", reversed_list)
