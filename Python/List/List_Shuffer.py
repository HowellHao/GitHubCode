import random
number = random.sample(range(0, 150), 15)
print("Original List: ", number)
number.sort(reverse=True)
print("Sorted List: ", number)