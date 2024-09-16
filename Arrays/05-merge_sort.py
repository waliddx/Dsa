"""
The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays,
and then building the array back together the correct way so that it is sorted.
"""

def merge(left, right):
    ''' function return merged values given in left and right lists sorted '''
    merged = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def mergeSort(array):
    step = 1    # Starting with sub-arrays of length 1
    length = len(array)

    while step < length:
        for i in range(0, length, 2*step):
            left = array[i:(i+step)]
            right= array[(i+step):(i+2*step)]

            merged = merge(left, right)
            # Place the merged array back into the original array
            for index, value in enumerate(merged):
                array[(i+index)] = value
        
        step *= 2   # Double the sub-array length for the next iteration

# test Array:
my_array = [3, 7, 6, -10, 15, 23, 55, -13, 24]
mergeSort(my_array)
print(my_array)