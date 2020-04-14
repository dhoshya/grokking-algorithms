def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selectionSort(arr):
    result = []
    for i in range(len(arr)):
        # finds index of smallest element in the array
        smallest = findSmallest(arr)
        # pops that element from the given array
        # and appends it to the result array
        result.append(arr.pop(smallest))

    return result


print(selectionSort([5, 3, 6, 2, 10]))
