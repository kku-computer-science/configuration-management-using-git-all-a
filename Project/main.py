# Author: Kantavich Suri (หรือชื่อเพื่อนคนที่ 3 ที่รับผิดชอบ Main)
# Description: Main program to run Quick Sort and Bubble Sort

import time
import sys

# Import ฟังก์ชันจากไฟล์ของเพื่อน
try:
    from bubble_sort import bubble_sort
    from quick_sort import quick_sort
except ImportError as e:
    print(f"❌ Error: Missing module. Please ensure bubble_sort.py and quick_sort.py exist.")
    print(f"   Details: {e}")
    sys.exit(1)


def get_user_input():
    """รับค่า Input จาก User และแปลงเป็น List of Integers"""
    while True:
        try:
            val_str = input("Enter integers (comma separated, e.g., 5, 12, 9): ").strip()
            
            # อนุญาตให้ผู้ใช้พิมพ์ 'q' เพื่อออกจากโปรแกรม
            if val_str.lower() == 'q':
                print("Exiting program...")
                sys.exit(0)
            
            if not val_str:
                print("⚠️  No data entered. Please try again or press 'q' to quit.")
                continue
            
            # แปลง string เป็น list ของ int และตัดช่องว่างออก
            data = [int(x.strip()) for x in val_str.split(',')]
            
            if len(data) == 0:
                print("⚠️  No valid integers found. Please try again.")
                continue
            
            return data
            
        except ValueError:
            print("❌ Error: Invalid input! Please enter only integers separated by commas.")
            print("   Example: 5, 12, 9, 3, 21")


def display_header():
    """แสดงหัวข้อโปรแกรม"""
    print("\n" + "=" * 50)
    print("      🔢 Sorting Algorithm Application 🔢")
    print("=" * 50)


def get_algorithm_choice():
    """รับการเลือก Algorithm จากผู้ใช้"""
    while True:
        print("\n📋 Select Sorting Algorithm:")
        print("   [1] Quick Sort  (by Worachat)  - Fast O(n log n)")
        print("   [2] Bubble Sort (by Krit)      - Simple O(n²)")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        if choice in ['1', '2']:
            return choice
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")


def get_sort_order():
    """รับรูปแบบการเรียงลำดับจากผู้ใช้"""
    while True:
        order = input("\n🔄 Sort Order (A=Ascending, D=Descending) [Default: A]: ").strip().upper()
        
        if order == '' or order == 'A':
            return False, "Ascending"
        elif order == 'D':
            return True, "Descending"
        else:
            print("❌ Invalid input! Please enter 'A' or 'D'.")


def display_data_info(data):
    """แสดงข้อมูลเบื้องต้นของ List"""
    print(f"\n📊 Original Data: {data}")
    print(f"   Size: {len(data)} elements")
    print(f"   Min: {min(data)}, Max: {max(data)}")
    print("-" * 50)


def main():
    display_header()
    
    # 1. รับข้อมูล (Input Data)
    data = get_user_input()
    display_data_info(data)
    
    # 2. เลือก Algorithm
    choice = get_algorithm_choice()
    
    # 3. เลือกรูปแบบการเรียง
    is_reverse, order_text = get_sort_order()
    
    # แสดงข้อมูลก่อนเริ่มประมวลผล
    algo_name = "Quick Sort" if choice == '1' else "Bubble Sort"
    print("-" * 50)
    print(f"🚀 Processing... (Algorithm: {algo_name}, Order: {order_text})")
    print("-" * 50)
    
    # 4. ประมวลผล (Processing) พร้อมสำเนาข้อมูลต้นฉบับ
    data_copy = data.copy()  # สำเนาเพื่อไม่ให้กระทบข้อมูลเดิม
    start_time = time.perf_counter()  # ใช้ perf_counter แทน time สำหรับความแม่นยำ
    
    try:
        if choice == '1':
            sorted_list = quick_sort(data_copy, reverse=is_reverse)
        else:  # choice == '2'
            sorted_list = bubble_sort(data_copy, reverse=is_reverse)
    except Exception as e:
        print(f"❌ Error during sorting: {e}")
        return
    
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000  # แปลงเป็น milliseconds
    
    # 5. แสดงผลลัพธ์ (Output)
    print(f"\n✅ {algo_name} Result: {sorted_list}")
    print(f"⏱️  Time taken: {elapsed_time:.4f} ms")
    
    # ตรวจสอบความถูกต้อง
    if sorted_list == sorted(data, reverse=is_reverse):
        print("✓  Sorting verified: CORRECT")
    else:
        print("⚠️  Warning: Sorting result may be incorrect")
    
    print("=" * 50)
    
    # ถามว่าต้องการทำต่อหรือไม่
    print("\n🔄 Sort another list? (Y/N): ", end="")
    if input().strip().upper() == 'Y':
        main()  # เรียกตัวเองใหม่
    else:
        print("\n👋 Thank you for using the Sorting Application!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user. Exiting...")
        sys.exit(0)