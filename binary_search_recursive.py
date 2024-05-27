# Performs a binary search on a sorted list to find the index of a specified key and prints the index if found,
# or -1 if the key is not present in the list.

def binary_search(array, lower, higher, key):
    if higher >= lower:
        mid = (higher + lower) // 2

        if array[mid] == key:
            return mid

        # must be left
        elif array[mid] > key:
            return binary_search(array, lower, mid - 1, key)

        # must be right
        else:
            return binary_search(array, mid + 1, higher, key)

    else:
        return -1


num_array = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]
find_n = 3

print(binary_search(array, 0, len(num_array) - 1, find_n))
