""" Python program for implementation of Bubble Sort.
Code originally from: https://www.geeksforgeeks.org/bubble-sort/"""


def bubble_sort(arr):
    """ Time Complexity O(n ** 2)"""

    n = len(arr)

    # Show steps during iterations, and not mandatory for Bubble Sort.
    outer_loop_result = 0
    inner_loop_result = 0

    # Outer loop, loop over all elements in the array.
    for outer_loop in range(n):
        outer_loop_result += 1
        inner_loop_result = 0
        print(f"Result: {outer_loop_result} ==> {arr}")

        # Inner loop.
        # NOTE: Loop is (n - 2) to avoid index out of range when swap last two
        # elements.
        for inner_loop in range(n - outer_loop - 1):
            # If left element greater than its next element, swap them.
            if arr[inner_loop] > arr[inner_loop + 1]:
                arr[inner_loop],
                arr[inner_loop + 1] = arr[inner_loop + 1], arr[inner_loop]

            inner_loop_result += 1
            print(f"    Inner: {inner_loop_result} ==> {arr}")


arr = [5, 3, 1, 9, 8, 2, 4, 7]

bubble_sort(arr)

print((5 * '\n') + "Sorted array is:")
for i in arr:
    print(i)