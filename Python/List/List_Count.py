import random
from collections import Counter

number = random.choices(range(0, 100), k=15)
print("Original List: ", number)

count_number = Counter(number)
print("Count of each number: ", count_number)