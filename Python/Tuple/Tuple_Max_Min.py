create_Tuple = tuple(map(int, input("Enter the elements for the new tuple separated by space: ").split(' ')))
print(create_Tuple)
max_element = max(create_Tuple)
min_element = min(create_Tuple)
print(f"The maximum element in the tuple is {max_element}.")
print(f"The minimum element in the tuple is {min_element}.")