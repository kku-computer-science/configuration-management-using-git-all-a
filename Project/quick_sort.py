# Author: Worachat Paranya (ID: 663380399-6)
# Description: Quick Sort Algorithm Implementation

import time
import random
from typing import List, Union

def quick_sort(arr: List[int], reverse: bool = False) -> List[int]:
    """
    Sorts a list of integers using the Quick Sort algorithm (Recursive).
    
    This implementation uses the 'Middle Pivot' strategy to improve performance
    on already sorted arrays and list comprehensions for readability.

    Args:
        arr (List[int]): The list of integers to sort.
        reverse (bool): If True, sort in descending order. Default is False.

    Returns:
        List[int]: A new list containing sorted elements.

    Time Complexity:
        - Best/Average: O(n log n)
        - Worst case: O(n^2) (rare with middle pivot)
    """
    
    # 1. Base Case: If the list is empty or has one element, it's already sorted.
    if len(arr) <= 1:
        return arr

    # 2. Pivot Selection:
    # Using the middle element is better than the first element (arr[0])
    # because it avoids O(n^2) performance on already sorted lists.
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    # 3. Partitioning:
    # Create three sub-lists for elements less than, equal to, and greater than pivot.
    # This explicitly handles duplicates correctly.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 4. Recursive Calls and Combine:
    if reverse:
        # For descending order: Greater -> Middle -> Less
        return quick_sort(right, reverse) + middle + quick_sort(left, reverse)
    else:
        # For ascending order: Less -> Middle -> Greater
        return quick_sort(left, reverse) + middle + quick_sort(right, reverse)

def measure_time(func, arr, reverse=False):
    """Helper function to measure execution time."""
    start_time = time.time()
    result = func(arr, reverse)
    end_time = time.time()
    print(f"Time taken: {(end_time - start_time) * 1000:.4f} ms")
    return result

# ==========================================
# Test Section (Main Execution)
# ==========================================
if __name__ == "__main__":
    print("=== Quick Sort Algorithm Test ===\n")

    # Test Case 1: Normal List
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Test 1 (Original): {test_data}")
    sorted_data = quick_sort(test_data)
    print(f"Test 1 (Sorted):   {sorted_data}")
    print("-" * 30)

    # Test Case 2: Already Sorted List (Performance Check)
    sorted_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Test 2 (Already Sorted): {sorted_input}")
    res_2 = quick_sort(sorted_input)
    print(f"Test 2 (Result):         {res_2}")
    print("-" * 30)

    # Test Case 3: Reverse Sort
    print("Test 3: Sorting in Descending Order (Reverse=True)")
    res_3 = quick_sort(test_data, reverse=True)
    print(f"Test 3 (Result): {res_3}")
    print("-" * 30)

    # Test Case 4: Large Dataset & Performance
    print("Test 4: Large Random Dataset (1,000 elements)")
    large_data = [random.randint(1, 10000) for _ in range(1000)]
    # Measure time
    measure_time(quick_sort, large_data)
    
    print("\nAll tests completed.")