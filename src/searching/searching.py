def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        midpoint = (start + end) // 2

        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            start = midpoint + 1
        else:
            end = midpoint - 1

    return -1  # not found
