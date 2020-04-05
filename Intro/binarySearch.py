def binary_search(searchArray, item):
    low = 0
    high = 4

    while low <= high:
        mid = (low + high)
        guess = searchArray[mid]
        if guess == item:
            print(guess)
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


binary_search([1, 3, 5, 7, 9], 3)
