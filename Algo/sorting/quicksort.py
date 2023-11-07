def quicksort(arr):
    # Step 1: Define the Quick Sort function
    def _quicksort(arr, low, high):
        if low < high:
            # Step 2: Partition the array and get the pivot index
            pivot_index = _hoare_partition(arr, low, high)
            
            # Step 3: Recursively sort the two subarrays
            _quicksort(arr, low, pivot_index)
            _quicksort(arr, pivot_index + 1, high)

    # Step 4: Define the Hoare Partition function
    def _hoare_partition(arr, low, high):
        pivot = arr[low]  # Choose the pivot as the first element
        i, j = low - 1, high + 1
        while True:
            # Step 4.1: Find an element on the left side that is greater than or equal to the pivot.
            while True:
                i += 1
                if arr[i] >= pivot:
                    break

            # Step 4.2: Find an element on the right side that is less than or equal to the pivot.
            while True:
                j -= 1
                if arr[j] <= pivot:
                    break

            # Step 4.3: If the left pointer (i) is greater than or equal to the right pointer (j),
            # we've found the correct position for the pivot, and the partitioning is complete.
            if i >= j:
                return j

            # Step 4.4: Swap the elements at positions i and j to move smaller elements to the left
            # and larger elements to the right.

            arr[i], arr[j] = arr[j], arr[i]

    # Step 5: Start the Quick Sort with the entire array
    _quicksort(arr, 0, len(arr) - 1)

# Step 6: Test the Quick Sort

import random
from datetime import datetime
arr = [random.randint(1, 10000) for _ in range(1000)]
print('array created')
s1 = datetime.now()
quicksort(arr)
print(f'time taken to sort {datetime.now() - s1}')
# print(arr)
