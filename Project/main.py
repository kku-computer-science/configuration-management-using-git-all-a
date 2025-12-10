# Author: Kantavich Suri (หรือชื่อเพื่อนคนที่ 3 ที่รับผิดชอบ Main)
# Description: Main program to run Quick Sort and Bubble Sort

import time
import sys

# Import ฟังก์ชันจากไฟล์ของเพื่อน
# หมายเหตุ: ต้องมีไฟล์ bubble_sort.py และ quick_sort.py อยู่ในโฟลเดอร์เดียวกัน
try:
    from bubble_sort import bubble_sort
    from quick_sort import quick_sort
except ImportError as e:
    print(f"Error: Missing module. Please ensure bubble_sort.py and quick_sort.py exist. ({e})")
    sys.exit(1)

def get_user_input():
    """รับค่า Input จาก User และแปลงเป็น List of Integers"""
    while True:
        try:
            val_str = input("Enter integers (comma separated, e.g. 5, 12, 9): ")
            if not val_str.strip():
                return [] # คืนค่าว่างถ้าไม่กรอกอะไร
            # แปลง string เป็น list ของ int และตัดช่องว่างออก
            data = [int(x.strip()) for x in val_str.split(',')]
            return data
        except ValueError:
            print(" Error: Invalid input! Please enter only integers separated by commas.")

def main():
    print("=========================================")
    print("    Sorting Algorithm Application    ")
    print("=========================================")

    # 1. รับข้อมูล (Input Data)
    data = get_user_input()
    if not data:
        print("No data entered. Exiting...")
        return

    print(f"\n Original Data: {data}")
    print("-" * 40)

    # 2. เลือก Algorithm
    print("Select Sorting Algorithm:")
    print(" [1] Quick Sort  (by Worachat)")
    print(" [2] Bubble Sort (by Krit)")
    
    choice = input("Enter choice (1 or 2): ").strip()

    # 3. เลือกรูปแบบการเรียง (Optional Feature)
    order = input("Sort Order (A=Ascending, D=Descending) [Default: A]: ").strip().upper()
    is_reverse = True if order == 'D' else False
    order_text = "Descending" if is_reverse else "Ascending"

    print("-" * 40)
    print(f"🚀 Processing... (Algorithm: {'Quick Sort' if choice == '1' else 'Bubble Sort'}, Order: {order_text})")

    # 4. ประมวลผล (Processing)
    start_time = time.time()
    
    if choice == '1':
        sorted_list = quick_sort(data, reverse=is_reverse)
        algo_name = "Quick Sort"
    elif choice == '2':
        sorted_list = bubble_sort(data, reverse=is_reverse)
        algo_name = "Bubble Sort"
    else:
        print("Invalid Choice! Exiting.")
        return

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000

    # 5. แสดงผลลัพธ์ (Output)
    print(f" {algo_name} Result: {sorted_list}")
    print(f" Time taken: {elapsed_time:.4f} ms")
    print("=========================================")

if __name__ == "__main__":
    main()