# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Loop through unsorted index
        for unsorted_index in range(cur_index + 1, len(arr)):
            # If the unsorted index value is < the current smallest value
            if arr[unsorted_index] < arr[smallest_index]:
                # Set that value as the new smallest value
                smallest_index = unsorted_index
        # Swap the new smallest value with the first unsorted position
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)

    # Loop through n-1 values
    for i in range(n-1):
    # range(n) also works but outer loop will repeat one time more than needed

        # Last i values are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the value found is greater
            # than the next value
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # If there's no values in the array
    if not arr:
        # Return empty array
        return arr

    # If any value in the array is less than 0, return
    # "Error, negative numbers not allowed in Count Sort"
    if any(x < 0 for x in arr):
        return "Error, negative numbers not allowed in Count Sort"
    
    # Else instantiate an array of 0s whose length is the max value + 1
    # (+1 because we start the count at 0)
    else:
        buckets = [0] * (max(arr) + 1)

    # Loop through the items in the array
    # (if list was [1, 2, 4, 2, 7, 5, 1])
    for i in range(len(arr)):
        # Take a count array to store the count of each unique object
        # Index:     0  1  2  3  4  5  6  7  8  9
        # Count:     0  2  2  0   1  1  0  1  0  0
        buckets[i] += 1
        # Modify the count array such that each element at each index 
        # stores the sum of previous counts; keep a running count 
        # Index:     0  1  2  3  4  5  6  7  8  9
        # Count:     0  2  4  4  5  6  6  7  7  7
        buckets[i] += buckets[i-1]
        # To output this into a sorted list, its saying that 1 is in slot 2,
        # then subtract 1 and put it in slot 1 as well. 2 is in slot 4, subtract
        # by one and also put it in slot 3 7:35 4 in slot 5, subtract by 1 and so on
        # to get [1,1,2,2,4,5,7]
        arr[i] = buckets[i] -1
    
    return arr
