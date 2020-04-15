# D&C
def quickSort(arr):
    # base case
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        # using list comprehension
        less = [i for i in arr[1:] if i <= pivot]
        # using normal syntax
        greater = list()
        for i in arr[1:]:
            if i >= pivot:
                greater.append(i)

        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([10, 5, 2, 3]))

