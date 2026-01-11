# Author: Krit Intarajinda (ID: 663380374-2) 
# Description: Bubble Sort Algorithm Implementation

import time
import random
from typing import List

def bubble_sort(arr: List[int], reverse: bool = False) -> List[int]:
    """
    Sorts a list of integers using the Bubble Sort algorithm.
    
    This implementation repeatedly steps through the list, compares adjacent
    elements, and swaps them if they are in the wrong order.

    Args:
        arr (List[int]): The list of integers to sort.
        reverse (bool): If True, sort in descending order. Default is False.

    Returns:
        List[int]: A new list containing sorted elements.

    Time Complexity:
        - Best case: O(n)       (when already sorted)
        - Average:  O(n^2)
        - Worst:    O(n^2)
    """

    n = len(arr)
    result = arr.copy()  # ทำสำเนาเพื่อไม่แก้ค่า list เดิม

    for i in range(n):
        swapped = False
        
        # วนลูปจนถึงตำแหน่ง n-i-1 (เพราะหลัง ๆ จะเรียงแล้ว)
        for j in range(0, n - i - 1):

            # เช็คเงื่อนไขการสลับ (Ascending หรือ Descending)
            if (not reverse and result[j] > result[j + 1]) or \
               (reverse and result[j] < result[j + 1]):

                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # ถ้าไม่มีการสลับเลย แสดงว่าเรียงเสร็จแล้ว
        if not swapped:
            break

    return result


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
    print("=== Bubble Sort Algorithm Test ===\n")

    # Test Case 1: Normal List
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Test 1 (Original): {test_data}")
    sorted_data = bubble_sort(test_data)
    print(f"Test 1 (Sorted):   {sorted_data}")
    print("-" * 30)

    # Test Case 2: Already Sorted List (Performance Check)
    sorted_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Test 2 (Already Sorted): {sorted_input}")
    res_2 = bubble_sort(sorted_input)
    print(f"Test 2 (Result):         {res_2}")
    print("-" * 30)

    # Test Case 3: Reverse Sort
    print("Test 3: Sorting in Descending Order (Reverse=True)")
    res_3 = bubble_sort(test_data, reverse=True)
    print(f"Test 3 (Result): {res_3}")
    print("-" * 30)

    # Test Case 4: Large Dataset & Performance
    print("Test 4: Large Random Dataset (1,000 elements)")
    large_data = [random.randint(1, 10000) for _ in range(1000)]
    
    # Measure time
    measure_time(bubble_sort, large_data)
    
    print("\nAll tests completed.")
