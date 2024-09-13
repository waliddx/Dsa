"""
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(1, n):
    swapped = True
    for j in range(1, n-i+1):
        if my_array[j] < my_array[j-1]:
            my_array[j], my_array[j-1]= my_array[j-1], my_array[j]
            swapped = False
    if swapped:
        break
print(my_array)
