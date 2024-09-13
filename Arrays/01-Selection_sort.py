"""
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
"""

my_array= [1, 64, 34, 1, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_idx]:
            min_idx = j
    my_array[i], my_array[min_idx] = my_array[min_idx], my_array[i]

print(my_array) # Output: [1, 1, 5, 11, 12, 22, 25, 34, 64, 90]
