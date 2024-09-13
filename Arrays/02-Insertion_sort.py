"""
The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(1, n):
    j = i
    while j > 0 and my_array[j-1] > my_array[j]:
        my_array[j-1], my_array[j] = my_array[j], my_array[j-1]
        j -= 1
print(my_array) # Output: [5, 11, 12, 22, 25, 34, 64, 90]
