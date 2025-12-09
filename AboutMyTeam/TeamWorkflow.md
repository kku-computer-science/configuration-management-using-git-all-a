# Team Workflow

## Team Members (สมาชิกและหน้าที่)
- **Member 1 (Worachat):** สร้าง Repo และโฟลเดอร์โครงสร้าง, เขียนและทดสอบ algorithm Quick Sort
- **Member 2 (Krit):** เขียนและทดสอบ algorithm Bubble Sort
- **Member 3 (Kantavich):** เขียน Main Program เพื่อรวบรวมฟังก์ชันและทำการทดสอบ Algorithm ทั้งสอง

## Workflow Process (ขั้นตอนการทำงาน)
1. **Initial Setup:** Member 1 (Worachat) สร้าง brach ของตัวเอง สร้างโฟลเดอร์ และ ไฟล์ที่จำเป็นเช่น AboutMyTeam, Project และ TeamWorkflow.md พร้อมส่งโค้ด algorithm Quick Sort ขึ้นไปที่ Main Branch เรียบร้อยแล้ว
2. **Pull & Branch:** สมาชิกคนอื่นๆ ต้องทำการ `git pull origin main` เพื่อดึงงานล่าสุดก่อน แล้วสร้าง Branch ส่วนตัว (`git checkout -b ชื่อ_รหัส`)
3. **Implementation:**
   - Member 2 (Krit) เขียนแนะนำตัวเองใน `AboutMyTeam/Krit_374-2.md` และเขียนโค้ด algorithm ใน `Project/bubble_sort.py`
   - Member 3 (Kantavich) เขียนแนะนำตัวเองใน `AboutMyTeam/Kantawit_586-7.md` และโค้ดใน `Project/main.py` 
4. **Merge & Push:** เมื่อเขียนและทดสอบเสร็จ ให้ Merge Branch ของตัวเองเข้ากับ Main (`git merge ...`) แล้ว Push ขึ้น GitHub
5. **Final Check:** ทุกคนช่วยกันตรวจสอบความถูกต้องบน GitHub และแก้ไข Conflict ร่วมกัน