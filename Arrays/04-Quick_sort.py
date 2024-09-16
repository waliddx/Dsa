"""
The Quicksort algorithm takes an array of values,
chooses one of the values as the 'pivot' element,
and moves the other values so that lower values are on the left of the pivot element,
and higher values are on the right of it.
"""

def get_median(arr, left, center, right):
    ''' function return the median out of three indexes '''
    if (arr[left] - arr[center]) * (arr[right] - arr[left]) >= 0:
        return left
    elif (arr[center] - arr[left]) * (arr[right] - arr[center]) >= 0:
        return center
    return right

def partition(arr, left, right):
    ''' function keeps swapping elements on the array till it faces the break point'''
    center = left + (right - left) // 2
    median_index = get_median(arr, left, center, right)

    arr[median_index], arr[right] =  arr[right], arr[median_index]
    pivot = arr[right]

    pivot_index = left-1
    for i in range(left, right):
        if arr[i] <= pivot:
            pivot_index += 1
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
    arr[pivot_index + 1], arr[right] = arr[right], arr[pivot_index + 1]

    return pivot_index + 1

def quicksort(arr, left=0, right=None):
    ''' main recursive function to keep on track of elements and sort them '''
    if right is None:
        right = len(arr)-1

    while left < right:
        pivot_index = partition(arr, left, right)    # it's considered as the center point

        if pivot_index - left < right - pivot_index:   # to choose which part to chose first left or right one
            quicksort(arr, left, pivot_index - 1)
            left = pivot_index + 1  # keep moving forward
        else:
            quicksort(arr, pivot_index + 1, right)
            right = pivot_index - 1 #keep moving forward

# Test array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print(my_array) # Output: [5, 11, 12, 22, 25, 34, 64, 90]
