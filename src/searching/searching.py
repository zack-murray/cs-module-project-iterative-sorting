def linear_search(arr, target):
    # Loop through the array 
    for i in range(len(arr)):
        # If the target is present in the array
        if arr[i] == target:
            # Return its location
            return i

    # We've reached outside the loop without finding the target value
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1 # because starting at 0

    # Loop through the array as long as low
    # of the index is <= the high of the index
    while low <= high:
        # Compare the target value to the midpoint
        mid = (high + low) // 2
        # If the target value equals the midpoint 
        if target == arr[mid]:
            # Return the target value
            return mid
        # If the target is < the midpoint
        if target < arr[mid]:
            # Cut out the right half of the array and reassign high to mid - 1
            high = mid - 1
        # If the target is > the midpoint
        if target > arr[mid]:
            # Cut out the left half of the array and reassign low to mid + 1 
            low = mid + 1

    # We've reached outside the loop without finding the target value
    return -1  # not found
