from patience_sort import patience_sort
from random_list import random_list

arr = random_list()

print(f"Array: {arr}")
arr = patience_sort(arr)
print(arr)